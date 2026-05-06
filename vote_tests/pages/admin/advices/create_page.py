from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class AdviceCreatePage(BasePage):
    NAME_INPUT = (By.NAME, "advice[name]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_name(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)).send_keys(name)
        return self

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        from pages.admin.advices.details_page import AdviceDetailsPage
        return AdviceDetailsPage(self.driver)