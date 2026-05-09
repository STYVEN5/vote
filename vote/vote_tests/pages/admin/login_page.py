from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class AdminLoginPage(BasePage):
    URL = "https://laratest.susu.ru/admin/login"

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "button-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".invalid-feedback")

    def open(self):
        super().open(self.URL)
        return self

    def enter_email(self, email: str):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        return self

    def enter_password(self, password: str):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
        return self

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text