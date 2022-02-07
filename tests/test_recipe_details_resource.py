import pytest
from ..recipes_api.constants import BASE_URL, RECIPE_DETAILS_ENDPOINT

def test_recipe_details(client):
    response = client.get(f"{BASE_URL}{RECIPE_DETAILS_ENDPOINT}garlicPasta")
    assert response.status_code == 200
    assert response.json == {
        "details":
            {
                "ingredients": [
                    "500mL water",
                    "100g spaghetti",
                    "25mL olive oil",
                    "4 cloves garlic",
                    "Salt"
                ],
                "numSteps":5
            }
    }

def test_recipe_details_empty(client):
    response = client.get(f"{BASE_URL}{RECIPE_DETAILS_ENDPOINT}sundaySauce")
    assert response.status_code == 200
    assert response.json == {}