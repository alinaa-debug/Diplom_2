from helpers.api_requests import post, get, patch, delete

def create_user(data):
    return post("auth/register", data=data)

def login_user(data):
    return post("auth/login", data=data)

def create_order(data, token=None):
    headers = {"Authorization" : f"Bearer {token}"} if token else None 
    return post("orders", data=data, headers=headers)

def get_user(token):
    return get("auth/user", {"Authorization" : f"Bearer {token}"})

def update_user(token, data):
    return patch("auth/user", data=data, headers={"Authorization" : f"Bearer {token}"})

def delete_user(token):
    return delete(
        "auth/delete",
         headers= {"Authorization" : f"Bearer {token}"})