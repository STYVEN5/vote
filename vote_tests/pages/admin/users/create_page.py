from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class UserCreatePage(BasePage):
    NAME_INPUT = (By.NAME, "user[name]")
    EMAIL_INPUT = (By.NAME, "user[email]")
    PASSWORD_INPUT = (By.NAME, "user[password]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_name(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)).send_keys(name)
        return self

    def fill_email(self, email: str):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        return self

    def fill_password(self, password: str = "testpass123"):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
        return self

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        from pages.admin.users.index_page import UsersIndexPage
        return UsersIndexPage(self.driver)