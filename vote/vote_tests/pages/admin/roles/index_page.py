from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage

class RolesIndexPage(BasePage):
    LIST_URL = "https://laratest.susu.ru/admin/roles"

    def open(self):
        super().open(self.LIST_URL)
        return self

    def click_add_button(self):
        add_btn = (By.CSS_SELECTOR, "a[href*='/admin/roles/create']")
        self.wait.until(EC.element_to_be_clickable(add_btn)).click()
        from pages.admin.roles.create_page import RoleCreatePage
        return RoleCreatePage(self.driver)

    def is_role_present(self, name: str) -> bool:
        row = (By.XPATH, f"//tr[.//span[normalize-space()='{name}']]")
        try:
            self.wait.until(EC.visibility_of_element_located(row))
            return True
        except TimeoutException:
            return False