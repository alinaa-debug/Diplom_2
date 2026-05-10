import requests
BASE_URL = "https://stellarburgers.education-services.ru/api"

def post(endpoint, data=None, headers=None):
    return requests.post(f"{BASE_URL}/{endpoint}", json=data, headers=headers)

def get(endpoint, headers=None):
    return requests.get(f"{BASE_URL}/{endpoint}", headers=headers)

def patch(endpoint, data=None, headers=None):
    return requests.patch(f"{BASE_URL}/{endpoint}", json=data, headers=headers)

