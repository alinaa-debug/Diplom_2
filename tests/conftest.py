import pytest
from helpers.user_helpers import create_user, login_user,delete_user
from data.data import generate_user
@pytest.fixture
def new_user():
    user = generate_user()
    response = create_user(user)
    token = response.json().get("accessToken")
    yield user, token
    if token:
        delete_user(token)

@pytest.fixture
def access_token(new_user):
    response = login_user(new_user)
    token = response.json().get("accessToken")
    if token and token.startswith("Bearer "):
        token = token.replace("Bearer ", "")
    return token
