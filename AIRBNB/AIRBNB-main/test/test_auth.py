#python -m pytest

import pytest
import requests
from assertpy import assert_that

BASE_URL = "http://127.0.0.1:8000"

def test_register_user_success():
    user_data = {
        "name": "Usuario Nuevo",
        "email": "usuario_nuevo@example.com",
        "password": "clave123"
    }
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()['message']).is_equal_to("Usuario registrado con éxito")

def test_register_user_failure():
    user_data = {
        "name": "Usuario Nuevo",
        "email": "usuario_nuevo@example.com",
        "password": "clave123"
    }
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(response.json()['message']).is_equal_to("El usuario ya existe")

def test_login_success():
    login_data = {
        "email": "usuario_nuevo@example.com",
        "password": "clave123"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['message']).is_equal_to("Inicio de sesión exitoso")
    assert_that(response.json()).contains("user_id")

def test_login_failure():
    login_data = {
        "email": "usuario_nuevo@example.com",
        "password": "clave_incorrecta"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert_that(response.status_code).is_equal_to(401)
    assert_that(response.json()['message']).is_equal_to("Credenciales inválidas")

def test_get_user_success():
    user_id = 1
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains("name", "email")

def test_get_user_fail_invalid_id():
    user_id = 9999
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert_that(response.status_code).is_equal_to(404)
