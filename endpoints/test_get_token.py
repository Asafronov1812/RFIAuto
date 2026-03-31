import pytest
from pages.homepage import HomePage

@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.order(1)
def test_get_token(jwt_token):
    HomePage(jwt_token).get_token()

