#python -m pytest

import requests
from assertpy import assert_that

BASE_URL = "http://127.0.0.1:8000"  

def test_create_property_success():
    property_data = {
        "name": "Casa en la playa",
        "location": "Cartagena",
        "price": 250.0
    }
    response = requests.post(f"{BASE_URL}/properties", json=property_data)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()['message']).is_equal_to("Propiedad creada con éxito")

def test_create_property_fail_missing_data():
    property_data = {
        "location": "Cartagena"
    }
    response = requests.post(f"{BASE_URL}/properties", json=property_data)
    assert_that(response.status_code).is_equal_to(422)

def test_get_property_success():
    property_id = 1
    response = requests.get(f"{BASE_URL}/property/{property_id}")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains("name", "location", "price")

def test_get_property_fail_invalid_id():
    property_id = 9999
    response = requests.get(f"{BASE_URL}/property/{property_id}")
    assert_that(response.status_code).is_equal_to(404)
