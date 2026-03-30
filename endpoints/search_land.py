import requests
from urllib3 import response


class SearchLand:
    response = None
    response_json = None

    def base_search_land(self):
        self.response = requests.post('https://rfi-core-service.apps.k8s.dev.pd15.sol.mtp/rfi-core/secured/api/v1/search-card/land?page=0&size=20&level=0')
        self.response_json = self.response.json()

    def check_search_response(self, size):
        # assert self.response_json['size'] == size
        assert response.HTTPResponse == 200