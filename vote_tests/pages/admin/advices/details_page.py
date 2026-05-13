from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class AdviceDetailsPage(BasePage):
    ADD_EVENT_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and .//span[contains(text(), 'Добавить мероприятие')]]")
    ADD_ADMIN_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and .//span[contains(text(), 'Добавить администратора')]]")
    TOAST = (By.CSS_SELECTOR, ".toast")

    def is_at_advice(self, name: str) -> bool:
        breadcrumb = (By.XPATH, f"//li[contains(@class, 'breadcrumb-item') and normalize-space()='{name}']")
        try:
            self.wait.until(EC.visibility_of_element_located(breadcrumb))
            return True
        except:
            return name in self.driver.title

    def click_add_event(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_EVENT_BUTTON))
        btn.click()
        from pages.admin.events.create_page import EventCreatePage
        return EventCreatePage(self.driver)

    def click_add_admin(self):
        # Дожидаемся исчезновения всплывающего уведомления
        try:
            self.wait.until(EC.invisibility_of_element_located(self.TOAST))
        except TimeoutException:
            pass
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_ADMIN_BUTTON))
        ActionChains(self.driver).move_to_element(btn).click().perform()
        from pages.admin.users.create_page import UserCreatePage
        return UserCreatePage(self.driver)