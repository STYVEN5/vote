from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class PollTemplateCreatePage(BasePage):
    NAME_INPUT = (By.NAME, "template[name]")
    OPTIONS_INPUT = (By.NAME, "template[options]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_name(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)).send_keys(name)
        return self

    def fill_options(self, options: str = "Да\nНет"):
        self.wait.until(EC.element_to_be_clickable(self.OPTIONS_INPUT)).send_keys(options)
        return self

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        from pages.admin.poll_templates.details_page import PollTemplateDetailsPage
        return PollTemplateDetailsPage(self.driver)