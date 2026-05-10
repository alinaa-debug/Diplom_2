from helpers.user_helpers import create_user, login_user
from data.data import generate_user, INVALID_USER

def test_user_login():
    user = generate_user()
    create_user(user)
    res = login_user(user)

    assert res.status_code == 200

    assert res.json()["success"] is True
    assert "accessToken" in res.json()

    res2 = login_user(INVALID_USER)
    assert res2.status_code == 401
    assert res2.json()["success"] is False
    assert res2.json()["message"] == "email or password are incorrect"