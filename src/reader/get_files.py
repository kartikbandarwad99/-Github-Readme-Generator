import requests

def list_github_files1(owner: str, repo: str, path: str = "", branch: str = "main"): #-> List[Dict]:
    print("Getting the list of files in a GitHub repository directory")
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url)
    response.raise_for_status()

    return [{"name": item["name"],
            "path": item["path"],
            "type": item["type"]} for item in response.json()]