from langchain_google_genai import ChatGoogleGenerativeAI
from src import read_github_file,list_github_files1
from src.Summarizer import Summarizer,ReadmeGenerator

def generate(owner,repo):

    all_files = list_github_files1(owner=owner, repo=repo)
    paths = [all_files[i]['path'] for i in range(len(all_files))]
    content = []
    for i in paths:
        try:
            response = read_github_file(
                owner=owner,
                repo=repo,
                path=i
            )
            print(f"{i} : Yes")
            content.append({i:response})
        except ValueError:
            print(f"{i} : Nay")

    summary_generator = Summarizer()
    readme_generator = ReadmeGenerator()

    summaries = {}

    # Summarize the individual .py and .ipynb files 
    for file_dict in content:
        for filename, code in file_dict.items():
            summary = summary_generator.summarize({filename: code})  
            summaries[filename] = summary

    # use the summaries to generate the readme file
    readme_sample = readme_generator.generate_readme(summaries)
    return readme_sample

if __name__ == '__main__':
    readme_sample = generate(owner = 'kartikbandarwad99',repo='Product_Hunt')
    with open("README.md", "w") as f:
        f.write(readme_sample.content)
    print("README.md has been generated successfully.")