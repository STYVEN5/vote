import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

class AdminLoginPage:
    URL = "https://vote.susu.ru/admin/login"

    # Локаторы, найденные по реальному HTML
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "input[name='remember']")
    LOGIN_BUTTON = (By.ID, "button-login")   # самый надёжный способ
    ADMIN_DASHBOARD_ELEMENT = (By.CSS_SELECTOR, ".sidebar, .dashboard")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, .invalid-feedback")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # увеличенный таймаут

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
        checkbox = self.wait.until(EC.element_to_be_clickable(self.REMEMBER_ME_CHECKBOX))
        if checkbox.is_selected() != check:
            checkbox.click()

    def click_login(self):
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()

    def get_error_message(self) -> str:
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text

    def is_login_successful(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.ADMIN_DASHBOARD_ELEMENT))
            return True
        except:
            return False

    # дополнительные методы для проверки полей (если нужны)
    def get_email_input(self):
        return self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))

    def get_password_input(self):
        return self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))

    def get_login_button(self):
        return self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))