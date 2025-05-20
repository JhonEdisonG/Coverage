#python -m pytest

import requests
from assertpy import assert_that

BASE_URL = "http://127.0.0.1:8000"  

def test_home_success():
    response = requests.get(f"{BASE_URL}/")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['message']).is_equal_to("Bienvenido a la API")

def test_home_fail_wrong_method():
    response = requests.post(f"{BASE_URL}/")
    assert_that(response.status_code).is_equal_to(405)
