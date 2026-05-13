from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SetupPage:
    URL = "https://laratest.susu.ru/tests"

    RESET_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][name='reset'][value='Сброс базы данных']")
    CREATE_ADMIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][name='create-admin'][value='Создание администратора']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_reset_db(self):
        reset_btn = self.wait.until(EC.element_to_be_clickable(self.RESET_BUTTON))
        reset_btn.click()
        time.sleep(1)

    def click_create_admin(self):
        admin_btn = self.wait.until(EC.element_to_be_clickable(self.CREATE_ADMIN_BUTTON))
        admin_btn.click()
        time.sleep(1)