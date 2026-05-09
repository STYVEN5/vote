from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class AdminMainPage(BasePage):
    URL = "https://laratest.susu.ru/admin/main"

    def open(self):
        super().open(self.URL)
        return self

    def go_to_advices(self):
        link = (By.XPATH, "//a[contains(@href, '/admin/advices')]")
        self.wait.until(EC.element_to_be_clickable(link)).click()
        from pages.admin.advices.index_page import AdvicesIndexPage
        return AdvicesIndexPage(self.driver)

    def go_to_poll_templates(self):
        link = (By.XPATH, "//a[contains(@href, '/admin/poll_templates')]")
        self.wait.until(EC.element_to_be_clickable(link)).click()
        from pages.admin.poll_templates.index_page import PollTemplatesIndexPage
        return PollTemplatesIndexPage(self.driver)

    def go_to_users(self):
        link = (By.XPATH, "//a[contains(@href, '/admin/users')]")
        self.wait.until(EC.element_to_be_clickable(link)).click()
        from pages.admin.users.index_page import UsersIndexPage
        return UsersIndexPage(self.driver)

    def go_to_roles(self):
        link = (By.XPATH, "//a[contains(@href, '/admin/roles')]")
        self.wait.until(EC.element_to_be_clickable(link)).click()
        from pages.admin.roles.index_page import RolesIndexPage
        return RolesIndexPage(self.driver)