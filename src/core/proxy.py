class AuthProxy:
    def __init__(self, method="api_key", key=None, token=None):
        self.method = method
        self.key = key
        self.token = token
        
    def get_headers(self):
        if self.method == "x_api_key":
            if not self.key:
                raise ValueError("API key is missing")
            return {"x-api-key": self.key}
        
        elif self.method == "jwt":
            if not self.token:
                raise ValueError("JWT token is missing")
            return {"Authorization": "Bearer " + self.token}
        
        elif self.method == "oauth":
            if not self.token:
                raise ValueError("OAuth token is missing")
            return {"Authorization": "OAuth " + self.token}
        
        elif self.method == "api_key":
            if not self.key:
                raise ValueError("API key is missing")
            return {"Authorization": "Bearer " + self.key}
        
        raise ValueError("Invalid authentication method: " + self.method)
    
    def get(self, url, params=None):
        import requests
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
