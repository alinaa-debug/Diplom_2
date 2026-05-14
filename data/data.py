import random

BASE_URL = "https://stellarburgers.education-services.ru/api"

class UserData:

    WITHOUT_EMAIL = {"password": "sfsv dfs",
                     "name": "ad"}
    
    WITHOUT_PASSWORD = {"email": "alina@gmail.com",
                     "name": "ad"}
    
    WITHOUT_NAME = {"email": "alina@gmail.com",
                 "password": "sfsv dfs"}
    
    FULL  = {"email": "alina@gmail.com",
                 "password": "sfsv dfs",
                 "name": "ad"}
    
    INVALID_LOGIN = {"email":"a@gmail.com",
                 "password": "1234567",
                 "name": "ad"}
    
    INVALID_PASSWORD = {"email":"alina@gmail.com",
                 "password": "1234567",
                 "name": "ad"}

class Ingridients:

    VALID_INGREDIENTS = '61c0c5a71d1f82001bdaaa6d'

    INVALID_INGREDIENTS = [
        "1234567",
        "0110000"    
    ]

class Burger:
    burger = {
        "ingredients": [Ingridients.VALID_INGREDIENTS]    
    }
