import pytest
from ..recipes_api.constants import BASE_URL, RECIPES_ENDPOINT

def test_recipe_names(client):
    response = client.get(f"{BASE_URL}{RECIPES_ENDPOINT}")
    assert response.status_code == 200
    assert response.json == {
        "recipeNames":
            [
                "scrambledEggs",
                "garlicPasta",
                "chai"
            ]
    }
    
def test_add_recipe(client):
    payload = {
        "name": "butteredBagel", 
        "ingredients": [
            "1 bagel", 
            "butter"
        ], 
        "instructions": [
            "cut the bagel", 
            "spread butter on bagel"
        ] 
    } 
    response = client.post(f"{BASE_URL}{RECIPES_ENDPOINT}", json=payload)
    assert response.status_code == 201
    
    
def test_add_recipe_negative(client):
    payload = {
        "name": "chai"
    }
    response = client.post(f"{BASE_URL}{RECIPES_ENDPOINT}", json=payload)
    assert response.status_code == 400
    assert response.json == {
        "error": "Recipe already exists"
    }
    
def test_update_recipe(client):
    payload = {
      "name": "scrambledEggs",
      "ingredients": [
        "1 tsp oil",
        "200 eggs",
        "salt"
      ],
      "instructions": [
        "Beat eggs with salt",
        "Heat oil in pan",
        "Add eggs to pan when hot",
        "Gather eggs into curds, remove when cooked",
        "Salt to taste and enjoy"
      ]
    }
    response = client.put(f"{BASE_URL}{RECIPES_ENDPOINT}", json=payload)
    assert response.status_code == 204
    
def test_update_recipe_negative(client):
    payload = {
        "name": "unbutteredBagel", 
        "ingredients": [
            "1 bagel"
        ], 
        "instructions": [
            "cut the bagel"
        ] 
    } 
    response = client.put(f"{BASE_URL}{RECIPES_ENDPOINT}", json=payload)
    assert response.status_code == 404
    assert response.json == {
        "error": "Recipe does not exist"
    }


