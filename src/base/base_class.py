import requests
import json


class BaseClass:
    def __init__(self, user, password):
        self.base_url = "https://habitica.com/api/v3"
        self.user = user
        self.password = password
        self.auth_header = {
            "content-type": "application/json",
            "x-api-user": self.user,
            "x-api-key": self.password,
        }

    def post_request(self, url, data):
        response = requests.post(url, headers=self.auth_header, data=json.dumps(data))
        return response.json()

    def get_request(self, url):
        response = requests.get(url, headers=self.auth_header)
        return response.json()

    def put_request(self, url, data):
        response = requests.put(url, headers=self.auth_header, data=json.dumps(data))
        return response.json()

    def delete_request(self, url):
        response = requests.delete(url, headers=self.auth_header)
        return response.json()

