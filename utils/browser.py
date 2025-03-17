from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import config.settings as settings

def get_browser():
    if settings.BROWSER.lower() == "chrome":
        options = ChromeOptions()
        if settings.HEADLESS:
            options.add_argument("--headless")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {settings.BROWSER}")
    return driver