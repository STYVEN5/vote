from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class PollTemplateDetailsPage(BasePage):
    def is_template_present(self, name: str) -> bool:
        # On details page, we can check title or a specific header
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[contains(@class, 'breadcrumb-item') and normalize-space()='{name}']")))
            return True
        except:
            return name in self.driver.title
