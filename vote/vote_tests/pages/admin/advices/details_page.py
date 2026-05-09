from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class AdviceDetailsPage(BasePage):
    ADD_EVENT_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and .//span[contains(text(), 'Добавить мероприятие')]]")
    ADD_ADMIN_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and .//span[contains(text(), 'Добавить администратора')]]")

    def is_at_advice(self, name: str) -> bool:
        from selenium.webdriver.support.ui import WebDriverWait
        # Check if name is in breadcrumbs or title with a shorter timeout for breadcrumb
        breadcrumb = (By.XPATH, f"//li[contains(@class, 'breadcrumb-item') and normalize-space()='{name}']")
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(breadcrumb))
            return True
        except:
            return name in self.driver.title

    def click_add_event(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_EVENT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()
        from pages.admin.events.create_page import EventCreatePage
        return EventCreatePage(self.driver)

    def click_add_admin(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_ADMIN_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()
        from pages.admin.users.index_page import UsersIndexPage
        return UsersIndexPage(self.driver)
