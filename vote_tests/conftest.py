import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    window_size = os.getenv("WINDOW_SIZE")
    if window_size:
        try:
            w, h = map(int, window_size.split(","))
            driver.set_window_size(w, h)
        except:
            driver.maximize_window()
    else:
        driver.maximize_window()
    yield driver
    driver.quit()