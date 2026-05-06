from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class RoleCreatePage(BasePage):
    NAME_INPUT = (By.NAME, "role[name]")
    SLUG_INPUT = (By.NAME, "role[slug]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_name(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)).send_keys(name)
        return self

    def fill_slug(self, name: str):
        slug = name.lower().replace(" ", "_")[:50]
        self.wait.until(EC.element_to_be_clickable(self.SLUG_INPUT)).send_keys(slug)
        return self

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        from pages.admin.roles.index_page import RolesIndexPage
        return RolesIndexPage(self.driver)