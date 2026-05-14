from helpers.api_requests import post, get, patch, delete
import string
import random

def create_user(payload):
    return post("auth/register", data=payload)

def login_user(payload):
    return post("auth/login", data=payload)

def create_order(payload, token=None):
    headers = {"Authorization" : f"Bearer {token}"} if token else None 
    return post("orders", data=payload, headers=headers)

def delete_user(token):
    return delete(
        "auth/delete",
         headers= {"Authorization": f"Bearer {token}"})


class RandomString:
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(
        random.choice(letters) for _ in range(length))       
        return random_string
