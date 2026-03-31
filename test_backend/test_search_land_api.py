import requests
import json
import pytest
from pages.homepage import HomePage
from endpoints.search_land_api import SearchLand

@pytest.mark.smoke
def test_search_land(jwt_token):
    token = HomePage(jwt_token).read_token()
    url = "http://rfi-core-service.apps.k8s.dev.pd15.sol.mtp/rfi-core/secured/api/v1/search-card/land?page=0&size=20&level=0"
    payload = json.dumps({
        "agencyId": "3245240187931858924"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    # response = requests.request("POST", url, headers=headers, data=payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
    # search_land = SearchLand()
    # search_land.check_search_response(200)

