from src import Get_Github_files,Fetch_file_content,ProcessURL,Summarizer
import time
import logging
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from src.Summarizer import Summarizer, ReadmeGenerator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RateLimitExceeded(Exception):
    pass

def summarize_repository(repo_dict, summarizer, path='', delay_between_retries=20, max_retries=3, timeout=10):
    summaries = {}
    SUPPORTED_EXTENSIONS = ('.py', '.ipynb')

    for key, value in repo_dict.items():
        current_path = f"{path}/{key}" if path else key
        if isinstance(value, dict):
            # It's a directory, recurse into it without passing the main summaries
            summaries[key] = summarize_repository(
                value,
                summarizer,
                current_path,
                delay_between_retries,
                max_retries,
                timeout
            )
        else:
            # It's a file, summarize it if supported
            if not key.endswith(SUPPORTED_EXTENSIONS):
                logging.info(f"Skipping unsupported file type: {current_path}")
                continue

            attempt = 0
            while attempt < max_retries:
                try:
                    with ThreadPoolExecutor(max_workers=1) as executor:
                        # Submit the summarize task
                        future = executor.submit(summarizer.summarize, {key: value})
                        # Wait for the result with a timeout
                        summary = future.result(timeout=timeout)
                    summaries[key] = summary.content
                    logging.info(f"Summarized {current_path}")
                    break  # Exit the retry loop upon success
                except TimeoutError:
                    attempt += 1
                    logging.warning(f"Timeout while summarizing {current_path}. Attempt {attempt} of {max_retries}. Retrying in {delay_between_retries} seconds...")
                except Exception as e:
                    attempt += 1
                    logging.warning(f"Error while summarizing {current_path}: {e}. Attempt {attempt} of {max_retries}. Retrying in {delay_between_retries} seconds...")

                if attempt < max_retries:
                    time.sleep(delay_between_retries)
                else:
                    logging.error(f"Failed to summarize {current_path} after {max_retries} attempts.")
                    summaries[key] = "Summary could not be generated due to repeated failures."

    return summaries

file_getter = Get_Github_files()
fetcher = Fetch_file_content()
url_processor = ProcessURL(fetcher=fetcher,file_getter=file_getter)

api_url = 'https://api.github.com/repos/kartikbandarwad99/Github-Readme-Generator/contents/'

repo_structure = {}
root_contents = file_getter.get_files(api_url=api_url)

for item in root_contents:
    key, value = url_processor.process(item)
    if value is not None:
        repo_structure[key] = value


summarizer_model = Summarizer()

summaries = summarize_repository(repo_structure,summarizer=summarizer_model)

readme_generator = ReadmeGenerator()
readme_sample = readme_generator.generate_readme(summaries=summaries)
print(readme_sample.content)