from helpers.user_helpers import create_order
from data.data import Burger, Ingridients


class TestCreateOrder:

    def test_create_order_auth_user(self, access_token):
        response = create_order(
            Burger.burger,
            access_token)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_order_not_auth_user(self):
        response = create_order(Burger.burger)
        assert response.status_code == 200
        assert response.json()["success"] is True


    def test_create_order_with_ingredients(
        self,
        access_token):
        response = create_order(
            Burger.burger,
            access_token)
        assert response.status_code == 200
        assert "order" in response.json()


    def test_create_order_without_ingredients(
        self,
        access_token):
        response = create_order(
            {"ingredients": []},
            access_token    )
        assert response.status_code == 400

    def test_create_order_invalid_ingredients(
        self,
        access_token):
        response = create_order(
            {
                "ingredients":
                    Ingridients.INVALID_INGREDIENTS
            },
            access_token)
        assert response.status_code == 500



