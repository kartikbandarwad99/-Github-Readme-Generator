# Github-Readme-Generator

## Description

This project automatically generates README files for GitHub repositories by summarizing the Python code within them. It fetches the contents of a specified repository, summarizes the Python files (.py and .ipynb) using a summarization model (Google Gemini LLM), and then generates a structured README.md file based on these summaries. The project handles directory structures recursively, summarizing files within subdirectories as well. It incorporates error handling with retries and timeout mechanisms for robustness, logging progress and issues along the way.

## File Structure

The project is structured as follows:

```
.
├── main.py                    # Main script to run the README generation process
└── src
    ├── __init__.py             # Initializes the package and imports key modules
    ├── reader
    │   ├── github_reader.py    # Fetches and processes files from GitHub
    │   └── get_files.py        # Retrieves file information from a GitHub repository
    └── Summarizer
        ├── __init__.py         # Initializes the Summarizer package
        └── summarizer.py      # Defines the Summarizer and ReadmeGenerator classes
```

## Installation

1.  Clone the repository: `git clone https://github.com/kartikbandarwad99/Github-Readme-Generator.git`
2.  Navigate to the project directory: `cd Github-Readme-Generator`
3.  Install the required packages: `pip install -r requirements.txt` (You'll need to create a `requirements.txt` file listing the project's dependencies, which would likely include `requests`, `langchain`, and `google-gemini`.)

## Usage

To generate a README for a specific GitHub repository, run the `main.py` script with the repository URL as an argument:

```bash
python main.py <github_repo_url>
```

For example:

```bash
python main.py kartikbandarwad99/Github-Readme-Generator
```

The generated README content will be printed to the console.  You can then redirect this output to a file:

```bash
python main.py kartikbandarwad99/Github-Readme-Generator > README.md
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests for bug fixes, feature enhancements, or improvements to the documentation.  If you plan to contribute new features or make substantial changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).  (You should create a `LICENSE` file containing the MIT License text.)
