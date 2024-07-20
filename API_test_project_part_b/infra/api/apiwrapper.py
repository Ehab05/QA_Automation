import requests


class APIWrapper:

    def __init__(self):
        pass

    def get_request(self, url, body=None, params=None, headers=None):
        try:
            return requests.get(url)
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def post_request(self, url, body=None, headers=None):
        try:
            return requests.post(url, json=body, headers=headers)
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def put_request(self, url, body=None, headers=None):
        try:
            return requests.put(url, json=body, headers=headers)
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

    def delete_request(self, url, headers=None):
        try:
            return requests.put(url, headers=headers)
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP:{e}")
        except Exception as e:
            print(f"Error: {e}")

