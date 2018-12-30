import requests
from bs4 import BeautifulSoup

def test_home_page():
    r = requests.get('http://localhost:80')

    soup = BeautifulSoup(r.content, 'html.parser')

    # check if search bar exists
    assert(soup.find("input", {"id": "search_value"}))

    assert(r.status_code == 200)

def test_query_python():
    r = requests.get('http://localhost:80/search?q=python')

    soup = BeautifulSoup(r.content, 'html.parser')

    # check if charts exists
    assert(soup.find("div", {"id": "chart_results"}))

    # check if top employer list exists
    assert(soup.find("div", {"id": "top_employers_chart_id"}))

    # check if top employer Pie chart exists
    assert(soup.find("div", {"id": "top_locations_chart_id"}))

    # check if top employer bar graph exists
    assert(soup.find("div", {"id": "top_langs_chart_id"}))

    assert(r.status_code == 200)
