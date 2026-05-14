import pytest
from helpers.user_helpers import create_user
from data.data import UserData


class TestCreateUser:

    def test_create_unique_user(self, create_random_user):
        response = create_user(create_random_user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_user_already_exists(
        self,
        create_and_delete_user):
        user = create_and_delete_user[1]
        response = create_user(user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @pytest.mark.parametrize(
        "payload",
        [
            UserData.WITHOUT_EMAIL,
            UserData.WITHOUT_PASSWORD,
            UserData.WITHOUT_NAME
        ]
    )
    def test_create_user_without_required_fields(
        self,
        payload):
        response = create_user(payload)
        assert response.status_code == 403



