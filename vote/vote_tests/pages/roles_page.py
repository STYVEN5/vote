import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RolesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    LIST_URL = "https://laratest.susu.ru/admin/roles"
    ADD_BUTTON = (By.CSS_SELECTOR, "a[href*='/admin/roles/create']")
    NAME_INPUT = (By.NAME, "role[name]")
    SLUG_INPUT = (By.NAME, "role[slug]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    DELETE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(text(), 'Удалить')]")

    def row_name_link(self, name: str):
        return (By.XPATH, f"//tr[.//span[normalize-space()='{name}']]//a")

    def row_by_name(self, name: str):
        return (By.XPATH, f"//tr[.//span[normalize-space()='{name}']]")

    def get_edit_url_from_row(self, name: str) -> str:
        link = self.wait.until(EC.presence_of_element_located(self.row_name_link(name)))
        href = link.get_attribute("href")
        return href + "/edit"

    def add_role(self, name: str):
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        time.sleep(1)
        name_field = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name_field.clear()
        name_field.send_keys(name)
        slug_value = name.lower().replace(" ", "_").replace(":", "").replace("-", "_")
        slug_field = self.wait.until(EC.presence_of_element_located(self.SLUG_INPUT))
        slug_field.clear()
        slug_field.send_keys(slug_value[:50])
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.row_by_name(name)))

    def is_role_present(self, name: str) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.row_by_name(name)))
            return True
        except TimeoutException:
            return False

    def edit_role(self, old_name: str, new_name: str):
        edit_url = self.get_edit_url_from_row(old_name)
        self.driver.get(edit_url)
        time.sleep(1)
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(new_name)
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.row_by_name(new_name)))

    def delete_role(self, name: str):
        edit_url = self.get_edit_url_from_row(name)
        self.driver.get(edit_url)
        time.sleep(1)
        del_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        del_btn.click()
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))
        confirm_btn.click()
        time.sleep(2)
        self.driver.get(self.LIST_URL)
        try:
            self.wait.until(EC.invisibility_of_element_located(self.row_by_name(name)))
        except:
            pass