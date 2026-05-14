import pytest
import allure

from helpers.user_helpers import login_user
from data.data import UserData


class TestLoginUser:

    def test_login_existing_user(self):
        response = login_user(UserData.FULL)
        assert response.status_code == 200
        assert response.json()["success"] is True

    
    @pytest.mark.parametrize(
        "payload",
        [
            UserData.INVALID_LOGIN,
            UserData.INVALID_PASSWORD
        ]
    )
    def test_login_invalid_user(self, payload):
        response = login_user(payload)
        assert response.status_code == 401
        assert response.json()["success"] is False


