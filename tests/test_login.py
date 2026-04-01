import pytest
from selenium.webdriver.common.by import By

# users = ['rfi_user', 'rfi_ca_user', 'rfi_user_mow']
# passwords = ['User_5511', 'User_4411', 'User_5511']

# def generate_pairs():
#     pairs = []
#     for user in users:
#         for password in passwords:
#             pairs.append(pytest.param((user, password), id=f'{user}, {password}'))
#     return pairs
#
# @pytest.mark.parametrize('creds', generate_pairs())

@pytest.mark.parametrize(
     'creds',
     [
         pytest.param(('rfi_user', 'User_5511'),id='rfi_user'),
         pytest.param(('rfi_ca_user', 'User_4411'),id='rfi_ca_user'),
         pytest.param(('rfi_user_mow', 'User_5511'),id='rfi_user_mow')
     ]
 )

@pytest.mark.skip
def test_login(creds, driver):
    username, password = creds
    driver.get('http://admin.dev.pd15.rosim.mtp/rfi/')
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "kc-login").click()
    temp = driver.find_element(By.CSS_SELECTOR, 'div[class="dashboard-card calendar-card"] h3').text
    assert temp == 'Календарь событий'