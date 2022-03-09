from pytest_bdd import given,when,then,scenario, parsers
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException
from conftest import user_for_url, user_rep_space_names, chrome_driver


#TODO: Missing validations
#TODO: make it gherkin-BDD style
#TODO executable path is different if run on windows not mac
test_location = '/Users/mormika/Downloads/chromedriver'
url_knime = "https://www.knime.com/"
url_knime_login = 'https://www.knime.com/user/login?destination=/'

class User():
	def __init__(self, username, password):
		self.username = username
		self.password = password

"""
Test data
"""
knime_user = User('Test_Knime_001', 'Jelszo')
spacename = "macska6"


"""
Login and navigating to User's space
"""
def login():
	chrome_driver.get(url_knime_login)
	chrome_driver.maximize_window()
	button_cookie_accept = chrome_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[1]')
	button_cookie_accept.click()
	field_user_name = chrome_driver.find_element(By.ID, 'edit-name')
	field_user_pw = chrome_driver.find_element(By.ID, 'edit-pass')
	button_sign_in = chrome_driver.find_element(By.ID, 'edit-submit')

	print("filling sign in fields and clicking")

	field_user_name.send_keys(knime_user.username)
	field_user_pw.send_keys(knime_user.password)
	button_sign_in.click()

	chrome_driver.implicitly_wait(2)

	# go to hub
	button_hub = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div/nav[1]/ul/li[1]/a')
	button_hub.click()
	chrome_driver.implicitly_wait(3)
	wait = WebDriverWait(chrome_driver, 5)
	wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#__layout > div > div.container.cookie-modal.modal.info > div.wrapper > div > div.controls > button"))).click()
	print("Found AND CLICKED the cookie element")
	# need to click on sign in again - not the smoothest

	button_sign_in_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/header/nav/div[2]/button')))
	button_sign_in_2.click()

	# go to spaces
	button_user_navigation = chrome_driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/header/nav/div[2]/div/button/div')
	button_user_navigation.click()

	button_spaces = chrome_driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/header/nav/div[2]/div/ul/li[2]/a")
	button_spaces.click()




"""
Creating a space
"""
login()
wait = WebDriverWait(chrome_driver, 10)
time.sleep(3)
chrome_driver.implicitly_wait(2)
print("trying to create a new space")
spacenames = user_rep_space_names(user_for_url)
count_spaces= len(spacenames)
print(count_spaces)
if count_spaces== 0:
	print("Currently there are 0 spaces")
	wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#__layout > div > div.sticky-footer > main > section > div > div.grid-item-9.child-container > div > div > ul > li > div > div > button:nth-child(2)'))).click()
else:
	try:
		count_spaces+=1
		wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#__layout > div > div.sticky-footer > main > section > div > div.grid-item-9.child-container > div > div > ul > li:nth-child({count_spaces}) > div > div > button:nth-child(2)'))).click()
		print("locating Webelement for space creation was successful")

	except TimeoutException:
		print("WebElement was not found! Inspect and correct the locator")


print(f"Name of the new public space:{spacename}")
if spacename in spacenames:
    print(f"WARNING: The {spacename} that you're trying to create is already in use!")
    raise Exception
else:
    print(f"The {spacename} is not used.")

time.sleep(2)
field_new_space = chrome_driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section[1]/div/div/div/div[1]/h3/div/div/textarea')
field_new_space.clear()
chrome_driver.implicitly_wait(2)
field_new_space.send_keys(f"{spacename}")
print("written in the name of the new space")
button_confirm_new_space_name = chrome_driver.find_element(By.XPATH, '//button[@title="Save"]')
button_confirm_new_space_name.click()
print("New space has been created")
time.sleep(2)

"""
Deleting space
"""

chrome_driver.implicitly_wait(2)
button_spaces = chrome_driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/section/nav/ul/li[3]/a')
button_spaces.click()

spacename_to_delete = spacename

print(f"Name of the public space you wish to delete:{spacename_to_delete}")

spacenames = user_rep_space_names(user_for_url)
count_spaces= len(spacenames)
if spacename_to_delete not in spacenames:
    print(f"WARNING: The {spacename} that you're trying to delete is not existing!")
    raise Exception
else:
    print(f"The {spacename_to_delete} can be deleted.")

chrome_driver.implicitly_wait(3)

button_space_to_delete = wait.until(EC.element_to_be_clickable(chrome_driver.find_element(By.XPATH, f'//h3[contains(text(), "{spacename_to_delete}")]'))).click()

chrome_driver.maximize_window()
wait = WebDriverWait(chrome_driver, 10)
button_new_space_more = wait.until(EC.element_to_be_clickable(chrome_driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/main/section[2]/div/div[2]/div[2]/div[3]/div/button'))).click()

button_delete_space = chrome_driver.find_element(By.XPATH, '//button[contains(text(), "Delete space")]')
button_delete_space.click()

#confirm that you wanna delete it
field_delete_space = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirmationForm"]/div/input')))
field_delete_space.send_keys(spacename_to_delete)
button_delete_space_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "I understand the consequences, delete space permanently")]')) )
button_delete_space_confirm.click()
print(f"User succcessfuly deleted : {spacename_to_delete}")
chrome_driver.close()















