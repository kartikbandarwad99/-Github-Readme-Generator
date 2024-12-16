import requests

class Get_Github_files:
    def __init__(self,branch='main'):
        self.params = {'ref':branch}
    def get_files(self,api_url):
        response = requests.get(api_url,params=self.params).json()
        return [{"name": item["name"],
            "path": item["path"],
            "type": item["type"],
            "url":item['url'],
            "download_url":item['download_url']} for item in response
            ]