import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def browser():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    yield driver
    
    # Close the browser
    driver.quit()

def test_facebook_login(browser):
    email = "chandu.chilukamary@gmail.com"
    password = "*38anDU#"

    # Open Facebook
    browser.get("https://www.facebook.com/")

    # Find the email input field and enter the email
    email_input = browser.find_element(By.ID, "email")
    email_input.send_keys(email)

    # Find the password input field and enter the password
    password_input = browser.find_element(By.ID, "pass")
    password_input.send_keys(password)

    # Find the login button and click it
    login_button = browser.find_element(By.NAME, "login")
    login_button.click()

    # Wait for a few seconds to allow the login process to complete
    time.sleep(5)

    # Check if login was successful
    assert "login_attempt" not in browser.current_url, "Login failed. Please check your email and password."
    assert "facebook.com" in browser.current_url, "Login successful!"