import requests


class API:
    def __init__(self, host: str, token: str, port: int):
        self.url = host
        self.token = token
        self.port = port

    @property
    def auth(self):
        return {"Authorization": f"Bearer {self.token}"}

    def _post(self, endpoint, payload):
        url = f"{self.url}/{endpoint}"
        r = requests.post(url, json=payload, headers=self.auth)
        data = r.json()
        if "error_code" in data:
            raise Exception(f'{data["error_code"], data["error_message"]}')
        return data

    def _get(self, endpoint, params):
        url = f"{self.url}/{endpoint}"
        r = requests.get(url, headers=self.auth, params=params)
        data = r.json()
        if "error_code" in data:
            raise Exception(f'{data["error_code"], data["error_message"]}')
        return data
