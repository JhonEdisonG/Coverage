#python -m pytest

import requests
from assertpy import assert_that

BASE_URL = "http://127.0.0.1:8000"

def test_submit_feedback_success():
    feedback_data = {
        "id_booking": 1,
        "id_property": 1,
        "comments": "Muy buena experiencia",
        "rating": 5
    }

    response = requests.post(f"{BASE_URL}/feedback", json=feedback_data)

    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()['message']).is_equal_to("Feedback guardado")

def test_submit_feedback_failure_missing_field():
    feedback_data = {
        "id_booking": 1,
        "id_property": 1,
        "rating": 4
    }

    response = requests.post(f"{BASE_URL}/feedback", json=feedback_data)

    assert_that(response.status_code).is_equal_to(422)
    assert_that(response.json()).contains_key("detail")

def test_get_feedback_success():
    property_id = 1

    response = requests.get(f"{BASE_URL}/feedback/{property_id}")

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains("feedback")
    assert_that(response.json()["feedback"]).is_type_of(list)

def test_get_feedback_failure_invalid_property():
    property_id = 9999

    response = requests.get(f"{BASE_URL}/feedback/{property_id}")

    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()['message']).is_equal_to("Propiedad no encontrada o sin feedback")
