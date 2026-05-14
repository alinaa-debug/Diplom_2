
import pytest
from helpers.user_helpers import create_user, delete_user, RandomString


@pytest.fixture
def create_random_user():

    return {
        "email": f"{RandomString.generate_random_string()}@mail.ru",
        "password": RandomString.generate_random_string(),
        "name": RandomString.generate_random_string()
    }



@pytest.fixture
def create_and_delete_user(create_random_user):
    user = create_random_user
    res = create_user(user)
    token = res.json().get("accessToken").replace("Bearer ", "")
    yield res, user, token
    if token:
        delete_user(token)

@pytest.fixture
def access_token(create_and_delete_user):
    return create_and_delete_user[2]        



