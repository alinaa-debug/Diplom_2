import random

def generate_user():
    x = random.randint(1000, 9999)
    return {
        "email": f"user{x}@test.com",
        "password": "123456",
        "name": f"user{x}"  }

EXISTING_USER = {
    "email": "test@test.com",
    "password": "123456",
    "name": "test"}

INVALID_USER = {
    "email": "",
    "password": "123456",
    "name": ""}

VALID_INGREDIENTS = {
    "ingredients": [
        "609646e4dc916e00276b2870"]}

EMPTY_INGREDIENTS = {
    "ingredients": []}

INVALID_INGREDIENTS = {
    "ingredients": ["12345"]}
