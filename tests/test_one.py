import pytest
import requests
import csv
'''
@pytest.mark.regress
def test_one():
    assert True


@pytest.mark.regress
def test_two():
    assert True


@pytest.mark.smoke
def test_free():
    assert True
'''
''''
@pytest.mark.regress # mark --- маркер
def test_one():
    assert True


@pytest.mark.xfail(strict=True)  #xfai -- тест запускается но упадет
@pytest.mark.regress
def test_two():
    assert True


@pytest.mark.skip(reason="JIRA-123")  # skip -- reason= --тест   не запускается
@pytest.mark.smoke
def test_free():
    assert True

def test_url_status(base_url):
    target = base_url
    response = requests.get(url=target)
    assert response.status_code == 200

def test_url_status1(qwe):
    assert qwe == 1

# Example with single parameter
@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


# Example with several parameters
@pytest.mark.parametrize("param1,param2", [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8)
])
def test_two(param1, param2):
    assert (param1 + param2) % 3 == 0


# Example with nested parametrization
@pytest.mark.parametrize("param2", [1, 2, 3, 4, 5])
@pytest.mark.parametrize("param1", [6, 7, 8, 9, 0])
@pytest.mark.parametrize("param3", [6, 7, 8, 9, 0])
def test_three_nested(param1, param2, param3):
    assert (param1 + param2) % 2 == 0
'''

def get_auth_endpoints():
    with open("auth_endpoints.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


auth_endpoints = get_auth_endpoints()

@pytest.mark.parametrize("data", auth_endpoints)
def test_with_generator(data):
    assert True