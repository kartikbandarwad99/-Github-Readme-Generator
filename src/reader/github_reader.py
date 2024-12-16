import requests

class Fetch_file_content:
    def __init__(self):
        pass
    def fetch(self,file_item):
        file_name = file_item['name']
        download_url = file_item.get('download_url')

        if file_name.endswith('.py'):
            response = requests.get(download_url)
            response.raise_for_status()
            return response.text
        elif file_name.endswith('.ipynb'):
            response = requests.get(download_url)
            response.raise_for_status()
            notebook = response.json()
            code = []
            for cell in notebook.get('cells', []):
                if cell.get('cell_type') == 'code':
                    code.append(''.join(cell.get('source', [])))
            return '\n\n'.join(code)
        else:
            pass

class ProcessURL:
    def __init__(self, fetcher, file_getter, branch="main", supported_extensions=('.py', '.ipynb')):
        self.fetcher = fetcher
        self.file_getter = file_getter
        self.branch = branch
        self.supported_extensions = supported_extensions

    def process(self, item):
        name = item['name']
        item_type = item['type']
        
        if item_type == 'file':
            if not name.endswith(self.supported_extensions):
                pass
            file_content = self.fetcher.fetch(item)
            return name, file_content

        elif item_type == 'dir':
            dir_contents = {}
            contents = self.file_getter.get_files(item['url'])
            for sub_item in contents:
                sub_key, sub_value = self.process(sub_item)  
                dir_contents[sub_key] = sub_value
            return name, dir_contents

        else:
            return name, None
