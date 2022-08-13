import requests

'''
def test_url_status(base_url):
    target = base_url + "breed/African/images/random"
    response = requests.get(url=target)
    assert response.status_code == 200


def test_invalid_date(base_url):
    res = requests.get(base_url + "breed/uncorrectbreed/images")
    assert res.status_code == 404
    assert res.json().get("status") == "error"
'''
def test_Ibizan(base_url):
    res = requests.get(base_url + "breed/african/images/random")
    assert res.status_code == 200
    assert res.json().get("status") == "success"
    assert res.json().get("message") == "https:\/\/images.dog.ceo\/breeds\/african\/n02116738_6117.jpg"