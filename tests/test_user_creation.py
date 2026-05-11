from helpers.user_helpers import create_user
from data.data import generate_user, EXISTING_USER, INVALID_USER


def test_user_creation():
    user = generate_user()
    res = create_user(user)

    assert res.status_code == 200
    assert res.json()["success"] is True

    res2 = create_user(EXISTING_USER)
    assert res2.status_code == 403
    assert res2.json()["message"] == "User already exists"

    res3 = create_user(INVALID_USER)
    assert res3.status_code == 403
    assert res3.json()["message"] == "Email, password and name are required fields"