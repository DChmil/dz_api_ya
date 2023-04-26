import requests

TOKEN = "***"


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        data = self.get_upload(file_path=disk_file_path)
        url = data.get('href')
        response = requests.put(url=url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload('test2.txt', 'test.txt')
