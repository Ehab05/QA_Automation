import requests


class APIWrapper:

    def __init__(self, base_url):
        self._base_url = base_url

    def get_request(self, endpoint, body=None, params=None, headers=None):
        url = self.get_url(endpoint)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def post_request(self, endpoint, data=None, headers=None):
        url = self.get_url(endpoint)
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def put_request(self, endpoint, data=None, headers=None):
        url = self.get_url(endpoint)
        try:
            response = requests.put(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def delete_request(self, endpoint, headers=None):
        url = self.get_url(endpoint)
        try:
            response = requests.put(url, headers=headers)
            response.raise_for_status()
            return response.status_code == 204
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def get_url(self, endpoint):
        if self._base_url:
            return f"{self._base_url}/{endpoint}"
        return None
