import pytest
from selenium.webdriver.common.by import By
from utils.browser import get_browser
import config.settings as settings
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("website", settings.WEBSITES)
def test_login(website):
    driver = get_browser()
    try:
        driver.get(website["url"])
        logger.info(f"Testing login for {website['name']}")

        # Assuming the login form has 'username' and 'password' fields and a 'submit' button
        driver.find_element(By.NAME, "username").send_keys(website["username"])
        driver.find_element(By.NAME, "password").send_keys(website["password"])
        driver.find_element(By.NAME, "submit").click()

        # Add assertions to verify successful login
        assert "Dashboard" in driver.title  # Example assertion, change as needed

    except Exception as e:
        logger.error(f"Login test failed for {website['name']}: {e}")
        raise
    finally:
        driver.quit()