import requests

def test_home_page():
    r = requests.get('http://localhost:80')

    assert(r.status_code == 200)

def test_query_python():
    r = requests.get('http://localhost:80/search?q=python')

    assert(r.status_code == 200)
