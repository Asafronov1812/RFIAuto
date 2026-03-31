import requests
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.homepage import HomePage




url = "http://rfi-core-service.apps.k8s.dev.pd15.sol.mtp/rfi-core/secured/api/v1/search-card/land?page=0&size=20&level=0"

payload = json.dumps({
  "agencyId": "3245240187931858924"
})
#получаем jwt токен
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
home_page = HomePage(driver)
home_page.open()
token = home_page.get_token()
driver.quit()

headers = {
  'Content-Type': 'application/json',
  'Authorization': token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
