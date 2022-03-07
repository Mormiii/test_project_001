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

# TODO: parallel excecution?!?!?
@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/ui_knime_hub.feature","Accessing spaces and UI verification")
def test_ui_verification():
    pass

@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/ui_knime_hub.feature","Creating a new public space")
def test_creating_space():
    pass

@pytest.mark.skip("reason=currently we dont want to test this")
@scenario("features/ui_knime_hub.feature","Deleting a space")
def test_deleting_space():
    pass




global test_location

test_location = '/Users/mormika/Downloads/chromedriver'
test_location_old= '/Applications/Google Chrome.app/Contents/MacOS/chromedriver'

# in case of installing the ChromeDriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())

url_knime = "https://www.knime.com/"
url_knime_login = 'https://www.knime.com/user/login?destination=/'


#TODO executable path is different if run on windows not mac



@given("logged in user with <username> and <password> viewing their spaces")
def login(username,password):
	chrome_driver = webdriver.Chrome(service=Service(test_location))
	chrome_driver.get(url_knime_login)
	chrome_driver.maximize_window()
	button_cookie_accept = chrome_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[1]')
	button_cookie_accept.click()
	field_user_name = chrome_driver.find_element(By.ID, 'edit-name')
	field_user_pw = chrome_driver.find_element(By.ID, 'edit-pass')
	button_sign_in = chrome_driver.find_element(By.ID, 'edit-submit')

	#filling sign in fields and clicking
	field_user_name.send_keys(f"{username}")
	field_user_pw.send_keys(f"{password}")
	button_sign_in.click()

	chrome_driver.implicitly_wait(2)

	# go to hub
	button_hub = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div/nav[1]/ul/li[1]/a')
	button_hub.click()

	chrome_driver.implicitly_wait(3)
	wait = WebDriverWait(chrome_driver, 5)
	#button_cookie_accept_2 = chrome_driver.find_element(By.CLASS_NAME, "accept-button button primary")
	#button_cookie_accept_2 = chrome_driver.find_element(By.CSS_SELECTOR, "#__layout > div > div.container.cookie-modal.modal.info > div.wrapper > div > div.controls > button")
	wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.container.cookie-modal.modal.info > div.wrapper > div > div.controls > button"))).click()
	print("Found AND CLICKED the cookie element")
	# sign in again ?! errror?

	button_sign_in_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/header/nav/div[2]/button')))
	button_sign_in_2.click()

	# go to spaces
	button_user_navigation = chrome_driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/header/nav/div[2]/div/button/div')
	button_user_navigation.click()

	button_spaces = chrome_driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/header/nav/div[2]/div/ul/li[2]/a")
	button_spaces.click()

# create new space
#chrome_driver.implicitly_wait(2)
#chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

@when("page is fully loaded")
def user_spaces_page():
	pass

@when("user creates a new public space with <spacename>")
def create_space(spacename):
	chrome_driver = webdriver.Chrome(service=Service(test_location))
	wait = WebDriverWait(chrome_driver, 10)
	chrome_driver.implicitly_wait(3)
	#wait.until(EC.visibility_of((By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section/div/div[2]/div/div/ul/li[9]/div/div/button[2]')))
	try:
		wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__layout > div > div.sticky-footer > main > section > div > div.grid-item-9.child-container > div > div > ul > li:nth-child(10) > div > div > button:nth-child(2)'))).click()
	except TimeoutException:
		wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section/div/div[2]/div/div/ul/li[9]/div/div/button[2]'))).click()

	new_space_name = 'Parampam1'

	#WebDriverWait(chrome_driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/main/section[1]/div/div/div/div[1]/h3/div/div/textarea")))
	print(f"Name of the new public space:{spacename}")
	field_new_space = chrome_driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section[1]/div/div/div/div[1]/h3/div/div/textarea')
	field_new_space.clear()

	field_new_space.send_keys(new_space_name)

	button_confirm_new_space_name = chrome_driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/main/section[1]/div/div/div/div[1]/h3/div/div/div/button[1]')
	button_confirm_new_space_name.click()

	# negativ testcase - name field is empty
@when("user deletes the choosen space with <spacename>")
def delete_space(spacename):
	chrome_driver = webdriver.Chrome(service=Service(test_location))
	# on spaces click on the space you wish to delete
	button_space_list = chrome_driver.find_element(By.CLASS_NAME, 'title')
	print(button_space_list)
	chrome_driver.implicitly_wait(3)
	button_space_details = chrome_driver.find_element(By.XPATH, '//*[ text() = {0} ]'.format(spacename))
	button_space_details.click()



	wait = WebDriverWait(chrome_driver, 10)
	button_new_space_more = chrome_driver.find_element(By.CSS_SELECTOR, '# __layout > div > div.sticky-footer > main > section.action-bar > div > div.grid-item-3.options > div:nth-child(2) > div:nth-child(3) > div > button > svg')
	button_new_space_more.click()

	button_delete_space = chrome_driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/button')
	button_delete_space.click()

	#confirm that you wanna delete it
	field_delete_space = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirmationForm"]/div/input')))
	field_delete_space.send_keys(spacename)
	button_delete_space_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[1]/main/section[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[4]/button')) )
	button_delete_space_confirm.click()

@then("verifying elements on the page")
def verify_ui():
	pass

@then("newly created space is visible under spaces")
def verfiy_created_space():
	pass

@then("the deleted space is no longer visible in spaces")
def verify_deleted_space():
	pass
## validation, no error
#def no_error_message(browser):
#	with pytest.raises(NoSuchElementException):
#		browser.find_element(By.CSS_SELECTOR, 'message error')

