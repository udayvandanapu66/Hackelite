
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
# Use forward slash for the path
geckodriver_path = "C:/Users/sahit/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe"

# Create a new instance of the Firefox driver with geckodriver path
browser = webdriver.Firefox(executable_path=geckodriver_path)

browser.get('https://fuelxpress.shop/')

if 'Fuel Xpress' in browser.title:
    print("Title verification passed!")
else:
    print("Title verification failed.")

# Perform login to the admin interface
admin_url = browser.current_url + 'admin'  # Fix the URL concatenation
browser.get(admin_url)  # Use the same browser instance

# Wait for the username field to be present
user_name = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)

user_password = browser.find_element_by_name('password')

user_name.send_keys('admin')
user_password.send_keys('1234')

login = browser.find_element_by_xpath('//input[@value="Log in"]')
login.click()

admin_title_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'title'))
)

# Get the text content of the title element on the admin page
admin_title_text = admin_title_element.get_attribute('innerText')

# Check if the expected text is present in the admin title
welcome_admin_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@id="user-tools"]/strong[text()="admin"]'))
)
welcome_admin_text = welcome_admin_element.get_attribute('innerText')
expected_text = "ADMIN"
if expected_text in welcome_admin_text:
    print("Welcome, admin. message verification passed!")
else:
    print("Welcome, admin. message verification failed.")
# Continue with other actions or assertions as needed


browser.get('https://fuelxpress.shop/')

# Interact with the list of links

create_account_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-outline-primary btn-block" and text()="Create Account"]'))
)

# Click the "Create Account" button
create_account_button.click()

browser.get('https://fuelxpress.shop/')

Login = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-primary btn-block" and text()="Login"]'))
)
Login.click()
time.sleep(30)

browser.get('https://fuelxpress.shop/u/login/')
user_name = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)

user_password = browser.find_element_by_name('password')

user_name.send_keys('admin')
user_password.send_keys('1234')

login_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-outline-info" and text()="Login"]'))
)

# Click the "Login" button
login_button.click()
# Don't forget to close the browser window when done
time.sleep(5)

browser.get("https://fuelxpress.shop/o/create/")

fuel_type_dropdown = browser.find_element(By.ID, "id_FX_fuel_type")
quantity_input = browser.find_element(By.ID, "id_FX_quantity")
cost_input = browser.find_element(By.ID, "id_FX_cost")
delivery_location_input = browser.find_element(By.ID, "id_FX_delivery_location")
csrf_token_input = browser.find_element(By.NAME, "csrfmiddlewaretoken")

# Set the values for each input field
fuel_type_dropdown.send_keys("Petrol")  # Replace with the desired value
quantity_input.send_keys("10")  # Replace with the desired value
cost_input.send_keys("50.00")  # Replace with the desired value
delivery_location_input.send_keys("Texas")  # Replace with the desired value

# Insert CSRF token value
csrf_token_value = csrf_token_input.get_attribute("value")

# Submit the form
order_form = browser.find_element(By.ID, "orderForm")
order_form.submit()
print("Order Created Successfully")
#browser.get(browser.current_url)
browser.get("https://fuelxpress.shop/o/list/")
print("Able to view Order successfully")
time.sleep(5)
browser.quit()


