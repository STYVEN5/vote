import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class Page():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_app_url(self) -> str:
        return os.environ.get("SITE_URL")

    def open(self, path: str):
        self.driver.get(self.get_app_url()+path)

    def assert_h1(self, text: str, timeout: int = 1):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), text)
        )
