import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_login_success():
    res = requests.post(f"{BASE_URL}/login", json={"username": "test_user", "password": "test_pass"})
    assert res.status_code == 200
    assert "token" in res.json()

def test_login_failure():
    res = requests.post(f"{BASE_URL}/login", json={"username": "invalid", "password": "wrong"})
    assert res.status_code == 401

def test_get_books():
    res = requests.get(f"{BASE_URL}/books")
    assert res.status_code == 200
    assert isinstance(res.json(), dict)

def test_order_book():
    login_res = requests.post(f"{BASE_URL}/login", json={"username": "test_user", "password": "test_pass"})
    token = login_res.json()["token"]
    res = requests.post(f"{BASE_URL}/order", json={"book_id": "1", "token": token})
    assert res.status_code == 200
    assert "ordered successfully" in res.json()["message"]

def test_delete_book():
    login_res = requests.post(f"{BASE_URL}/login", json={"username": "test_user", "password": "test_pass"})
    token = login_res.json()["token"]
    # First ensure the book exists
    requests.post(f"{BASE_URL}/order", json={"book_id": "2", "token": token})
    res = requests.delete(f"{BASE_URL}/book/2", params={"token": token})
    assert res.status_code == 200
    assert "deleted" in res.json()["message"]
