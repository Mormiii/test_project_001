import requests as REST
from json.decoder import JSONDecodeError
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException



token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2SHpuYUhTS3RMWmszcnczVlJBN2M4eThsUHlVazU3YndMejRvekFZT1o4In0.eyJqdGkiOiJmNmFiMThhZC1lMDczLTRmYWUtODI2YS0yNDA5YjNjNzU3MWMiLCJleHAiOjE2NDY4NDU1MjQsIm5iZiI6MCwiaWF0IjoxNjQ2ODM0NzI0LCJpc3MiOiJodHRwczovL2F1dGguaHViLmtuaW1lLmNvbS9hdXRoL3JlYWxtcy9rbmltZSIsInN1YiI6IjBlY2UwMmY1LWFkZmItNDU3Yi1hMmFmLWJjOTNkYjc0NDdjMCIsInR5cCI6IkJlYXJlciIsImF6cCI6Imh1Yi11aSIsIm5vbmNlIjoiR1l3aWxDejdKUVlMMU9xOXVGRExUTXloUDZYaXMxT1M1WnFsNEhEREVOMCIsImF1dGhfdGltZSI6MTY0NjgzNDcyNCwic2Vzc2lvbl9zdGF0ZSI6IjUxZjVkNjhmLTk5NzAtNDNjYy04ODk3LWQ4MmQyN2NhNzc5OCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zdGFnZS5odWIua25pbWUuY29tIiwiaHR0cHM6Ly9odWIua25pbWUuY29tIl0sInJlc291cmNlX2FjY2VzcyI6eyJicm9rZXIiOnsicm9sZXMiOlsicmVhZC10b2tlbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHJvbGVzIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlRlc3RfS25pbWVfMDAxIiwiZ3JvdXBzIjpbImh1YnVzZXIiXSwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdF9rbmltZV8wMDEiLCJnaXZlbl9uYW1lIjoiVGVzdF9LbmltZV8wMDEiLCJlbWFpbCI6ImRvci5kZWthbnlAZ21haWwuY29tIn0.SCR8u2_yk4VUZAsNIIhzE95WCS0N8OD_bRokTsGEiPz-k4GRu6vD6DP4xIh0RYshg6Sq7_EJDX1eYUk94ehEHyGeEFX0bjJjGb-8Umhc96K-6gVpeD9m6OqhgTE25z6BMMW-Fz27ps-Tjvf5z1OdFROCZfriOVf9xkhzAUxhRCQRjvmx-YS7lFT-tl7jM3eEAlKpvpJaWS2-toOx2qvi7WU1iQgyfulJZCZoadAtRNdJYAEJ94_FS81YZ-VBOt9hUIfImINo_CFMCBimGk0xVRVejdLU2FrdsAkEC30_QHNuzS1XoyCaNpAua3mOiURFg17JzCUTw9EHh2I1e_OXNQ"

test_location = '/Users/mormika/Downloads/chromedriver'
url_knime_login = 'https://www.knime.com/user/login?destination=/'

# here pls give the User for the repository
@pytest.fixture
def user():
	return 'test_knime_001'

user_for_url= 'test_knime_001'

#@pytest.fixture
#def chrome_driver():
#	return webdriver.Chrome(service=Service(test_location))


chrome_driver= webdriver.Chrome(service=Service(test_location))

def user_rep_space_names(user):
	# user = 'test_knime_001'
	url_user_repo = f'https://api.hub.knime.com/repository//Users/{user}'
	print(url_user_repo)
	params_space_details = {"spaceDetails": "true", "contribSpaces": "children"}
	print(f"Information about this user: {user}'s repository")
	#print("Sending a GET request to this url:", url_user_repo)
	headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
	resp = REST.get(url_user_repo, params=params_space_details, headers=headers)
	try:
		resp_json = resp.json()
	except JSONDecodeError:
		print("You're token might be invalid/expired!")
		raise Exception

	print("Number of spaces existing in this repository: ", len(resp_json["children"]))
	spaces = resp_json["children"]
	paths = []
	for i in spaces:
		paths.append(i['path'])
	#print(f" User has following children paths:{paths}")
	space_names = []
	for p in paths:
		#space_names.append(p.lstrip(f"/Users/{user}/"))
		space_names.append(p[22:])
	print(f"User has spaces with name: {space_names}")
	return space_names


"""
finding multiple elements and printing their attributes
"""


#button_multiple = chrome_driver.find_elements(By.TAG_NAME,'button')
#print(f"Buttons found: {button_multiple}")
#for i in button_multiple:
#	print(i)
#	attrs= chrome_driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', i)
#	print(attrs)