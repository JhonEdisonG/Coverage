#python -m pytest

import requests
from assertpy import assert_that
from datetime import datetime, timedelta

BASE_URL = "http://127.0.0.1:8000"

def test_create_reservation_success():
    user_id = 1
    property_id = 1
    in_time = datetime.now().date()
    out_time = in_time + timedelta(days=2)

    reservation_data = {
        "user_id": user_id,
        "property_id": property_id,
        "in_time": in_time.strftime("%Y-%m-%d"),
        "out_time": out_time.strftime("%Y-%m-%d")
    }

    response = requests.post(f"{BASE_URL}/reserve", json=reservation_data)

    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()['message']).is_equal_to("Reserva realizada con éxito")

def test_create_reservation_failure_invalid_dates():
    user_id = 1
    property_id = 1
    in_time = datetime.now().date()
    out_time = in_time - timedelta(days=1)

    reservation_data = {
        "user_id": user_id,
        "property_id": property_id,
        "in_time": in_time.strftime("%Y-%m-%d"),
        "out_time": out_time.strftime("%Y-%m-%d")
    }

    response = requests.post(f"{BASE_URL}/reserve", json=reservation_data)

    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.json()['message']).is_equal_to("La fecha de salida debe ser posterior a la fecha de entrada")

def test_create_reservation_failure_missing_fields():
    reservation_data = {
        "user_id": 1,
        "property_id": 1,
        "in_time": datetime.now().strftime("%Y-%m-%d")
    }

    response = requests.post(f"{BASE_URL}/reserve", json=reservation_data)

    assert_that(response.status_code).is_equal_to(422)
    assert_that(response.json()).contains_key("detail")
