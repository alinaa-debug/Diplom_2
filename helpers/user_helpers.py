from helpers.api_requests import post, get, patch

def create_user(data):
    return post("auth/register", data=data)

def login_user(data):
    return post("auth/login", data=data)

def create_order(data, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return post("orders", data=data, headers=headers)

def get_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    return get("auth/user", headers=headers)

def update_user(token, data):
    headers = {"Authorization": f"Bearer {token}"}
    return patch("auth/user", data=data, headers=headers)