import pytest
from helpers.user_helpers import create_user, login_user
from data.data import generate_user

@pytest.fixture
def new_user():
    user = generate_user()
    create_user(user)
    return user


@pytest.fixture 
def access_token(new_user): 
    response = login_user(new_user) 
    return response.json().get("accessToken").replace("Bearer ", "")