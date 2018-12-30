import requests

def test_home_page():
    r = requests.get('http://localhost:80')

    assert(r.status_code == 200)
