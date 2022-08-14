import requests
import pytest


@pytest.mark.smoke
def test_booking_post(base_url):
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url+"booking", json=info, headers=header)
    assert res.status_code == 200
    assert res.json().get("booking") == info



'''''

def test_booking_put(base_url):
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    res = requests.put(base_url, 'info')
    assert res.status_code == 200
    assert res.json().get("booking") == info


'''''

@pytest.mark.regress
def test_booking_delete_(base_url):
    info = {"username": "admin", "password": "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    token = res.json().get("token")
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "booking", json=info, headers=header)
    id1 = res.json().get("bookingid")
    cookie = "token=" + str(token)
    header = {"Content-Type": "application/json", "Cookie": cookie}
    res = requests.delete(base_url + "booking/" + str(id1), headers=header)
    assert res.status_code == 201


@pytest.mark.smoke
def test_booking_post_auth(base_url):
    info = {"username" : "admin", "password" : "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url+"auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_booking_post_no_pasword(base_url):
    info = {"userme" : "admin", "password" : ""}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_booking_post_no_login(base_url):
    info = {"userme" : "", "password" : "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_booking_post_no_log_pas(base_url):
    info = {"userme" : "", "password": ""}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200

@pytest.mark.regress
def test_booking_post_wrong_password(base_url):
    info = {"username" : "admin", "password" : "passw_111"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_booking_post_wrong_login(base_url):
    info = {"username" : "adm_123", "password" : "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200



