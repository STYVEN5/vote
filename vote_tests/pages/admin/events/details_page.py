from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class EventDetailsPage(BasePage):
    def go_back_to_advice(self, advice_name: str):
        # Use breadcrumb to go back
        breadcrumb = (By.XPATH, f"//li[contains(@class, 'breadcrumb-item')]//a[normalize-space()='{advice_name}']")
        self.wait.until(EC.element_to_be_clickable(breadcrumb)).click()
        from pages.admin.advices.details_page import AdviceDetailsPage
        return AdviceDetailsPage(self.driver)
