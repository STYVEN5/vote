from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class EventCreatePage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='event[name]']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_name(self, name: str):
        self.wait.until(EC.element_to_be_clickable(self.NAME_INPUT)).send_keys(name)
        return self

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        from pages.admin.events.details_page import EventDetailsPage
        return EventDetailsPage(self.driver)
