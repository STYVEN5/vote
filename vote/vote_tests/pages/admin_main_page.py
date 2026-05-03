from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminMainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    ACADEMIC_COUNCILS_LINK = (By.XPATH, "//a[contains(@href, '/admin/advices')]")
    VOTING_TEMPLATES_LINK = (By.XPATH, "//a[contains(@href, '/admin/poll_templates')]")
    USERS_LINK = (By.XPATH, "//a[contains(@href, '/admin/users')]")
    ROLES_LINK = (By.XPATH, "//a[contains(@href, '/admin/roles')]")

    def go_to_academic_councils(self):
        self.wait.until(EC.element_to_be_clickable(self.ACADEMIC_COUNCILS_LINK)).click()
        from pages.academic_councils_page import AcademicCouncilsPage
        return AcademicCouncilsPage(self.driver)

    def go_to_voting_templates(self):
        self.wait.until(EC.element_to_be_clickable(self.VOTING_TEMPLATES_LINK)).click()
        from pages.voting_templates_page import VotingTemplatesPage
        return VotingTemplatesPage(self.driver)

    def go_to_users(self):
        self.wait.until(EC.element_to_be_clickable(self.USERS_LINK)).click()
        from pages.users_page import UsersPage
        return UsersPage(self.driver)

    def go_to_roles(self):
        self.wait.until(EC.element_to_be_clickable(self.ROLES_LINK)).click()
        from pages.roles_page import RolesPage
        return RolesPage(self.driver)