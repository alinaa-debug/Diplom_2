from helpers.user_helpers import create_order
from data.data import VALID_INGREDIENTS, EMPTY_INGREDIENTS, INVALID_INGREDIENTS


class TestOrderCreation:
    def test_order_with_auth(self,access_token):
        res = create_order(VALID_INGREDIENTS, access_token)

        assert res.status_code == 200
        assert res.json()["success"] is True
        assert "orders" in res.json()


    def test_order_without_auth(self):
        res = create_order(VALID_INGREDIENTS)

        assert res.status_code == 401
        assert res.json()["success"] is False
        assert res.json()["message"] == "You should be authorised"


    def test_order_with_ingredients(self,access_token):
        res = create_order(VALID_INGREDIENTS, access_token)

        assert res.status_code == 200
        assert res.json()["success"] is True
        assert "orders" in res.json()


    def test_order_without_ingredients(self,access_token):
        res = create_order(EMPTY_INGREDIENTS, access_token)

        assert res.status_code == 400
        assert res.json()["success"] is False
        assert res.json()["message"] == "Ingredient ids must be provided"


    def test_order_invalid_ingredients(self,access_token):
        res = create_order(INVALID_INGREDIENTS, access_token)

        assert res.status_code == 500