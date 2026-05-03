import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

class UsersPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    LIST_URL = "https://laratest.susu.ru/admin/users"
    ADD_BUTTON = (By.CSS_SELECTOR, "a[href*='/admin/users/create']")
    NAME_INPUT = (By.NAME, "user[name]")
    EMAIL_INPUT = (By.NAME, "user[email]")
    PASSWORD_INPUT = (By.NAME, "user[password]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    DELETE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")

    def row_by_email(self, email: str):
        return (By.XPATH, f"//tr[contains(., '{email}')]")

    def edit_link_by_email(self, email: str):
        return (By.XPATH, f"//tr[contains(., '{email}')]//a[contains(@href, '/edit')]")

    def add_user(self, name: str, email: str, password: str = "testpass123"):
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.row_by_email(email)))

    def is_user_present(self, email: str) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.row_by_email(email)))
            return True
        except TimeoutException:
            return False

    def edit_user(self, old_email: str, new_name: str, new_email: str = None):
        edit_link = self.wait.until(EC.element_to_be_clickable(self.edit_link_by_email(old_email)))
        edit_link.click()
        time.sleep(1)
        name_input = self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT))
        try:
            name_input.clear()
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].value = '';", name_input)
        name_input.send_keys(new_name)
        if new_email:
            email_input = self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
            try:
                email_input.clear()
            except ElementNotInteractableException:
                self.driver.execute_script("arguments[0].value = '';", email_input)
            email_input.send_keys(new_email)
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        target_email = new_email if new_email else old_email
        self.wait.until(EC.presence_of_element_located(self.row_by_email(target_email)))

    def delete_user(self, email: str):
        edit_link = self.wait.until(EC.element_to_be_clickable(self.edit_link_by_email(email)))
        edit_link.click()
        time.sleep(1)
        del_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        del_btn.click()
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))
        confirm_btn.click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        try:
            self.wait.until(EC.invisibility_of_element_located(self.row_by_email(email)))
        except:
            pass