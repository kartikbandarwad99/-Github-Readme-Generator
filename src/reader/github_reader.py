import requests
import json

def read_github_file(owner, repo, path, branch="main"):
    print(f'Reading repo: {repo} by user:{owner}')
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    response = requests.get(url)
    response.raise_for_status()
    if not (path.endswith('.py') or path.endswith('.ipynb')):
        raise ValueError("Only .py and .ipynb files are supported")


    if path.endswith('.ipynb'):
        notebook = json.loads(response.text)
        code = []
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                code.append(''.join(cell['source']))
        return '\n\n'.join(code)
    else:
        return response.text