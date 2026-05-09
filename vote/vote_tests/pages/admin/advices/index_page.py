from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage

class AdvicesIndexPage(BasePage):
    LIST_URL = "https://laratest.susu.ru/admin/advices"

    def open(self):
        super().open(self.LIST_URL)
        return self

    def click_add_button(self):
        add_btn = (By.CSS_SELECTOR, "a[href*='/admin/advices/create']")
        self.wait.until(EC.element_to_be_clickable(add_btn)).click()
        from pages.admin.advices.create_page import AdviceCreatePage
        return AdviceCreatePage(self.driver)

    def is_advice_present(self, name: str) -> bool:
        row = (By.XPATH, f"//tr[.//span[normalize-space()='{name}']]")
        try:
            self.wait.until(EC.visibility_of_element_located(row))
            return True
        except TimeoutException:
            return False