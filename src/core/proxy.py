class AuthProxy:
    def __init__(self, method="api_key", key=None, token=None):
        self.method = method
        self.key = key
        self.token = token
        
    def get_headers(self):
        if self.method == "x_api_key":
            return {"x-api-key": self.key}
        elif self.method == "jwt":
            return {"Authorization": "Bearer " + self.token}
        elif self.method == "oauth":
            return {"Authorization": "OAuth " + self.token}
        elif self.method == "api_key":
            return {"Authorization": "Bearer " + self.key}
        return {}
    
    def get(self, url):
        import requests
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()
    