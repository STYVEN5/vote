import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()

class AdminLoginPage:
    URL = "https://laratest.susu.ru/admin/login"

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='remember']")
    LOGIN_BUTTON = (By.ID, "button-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, .invalid-feedback")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def enter_email(self, email: str):
        field = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        field.clear()
        field.send_keys(email)

    def enter_password(self, password: str):
        field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def check_remember_me(self, check: bool = True):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(self.REMEMBER_ME_CHECKBOX))
            if checkbox.is_selected() != check:
                checkbox.click()
        except TimeoutException:
            pass

    def click_login(self):
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()

    def get_error_message(self) -> str:
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text

    def is_login_successful(self) -> bool:
        # Ожидаем, что URL изменится и будет содержать '/admin/main'
        try:
            self.wait.until(lambda driver: "/admin/main" in driver.current_url)
            return True
        except TimeoutException:
            return False