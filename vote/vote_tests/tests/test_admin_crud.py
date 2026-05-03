import pytest
import os
from datetime import datetime
from pages.admin_main_page import AdminMainPage
from pages.admin_login_page import AdminLoginPage

class TestAdminCRUD:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = AdminLoginPage(driver)
        login_page.open()
        login_page.enter_email(os.getenv("ADMIN_EMAIL", "admin@laratest.susu.ru"))
        login_page.enter_password(os.getenv("ADMIN_PASSWORD", "R1j4rhnRZtC0bGi6"))
        login_page.click_login()
        login_page.wait.until(lambda d: "/admin/main" in d.current_url)
        self.main_page = AdminMainPage(driver)

    def test_academic_council_creation(self, driver):
        page = self.main_page.go_to_academic_councils()
        name = f"Совет {datetime.now():%Y-%m-%d %H:%M:%S}"
        page.add_council(name)
        assert page.is_council_present(name), "Совет не создан"

    def test_voting_template_creation(self, driver):
        page = self.main_page.go_to_voting_templates()
        name = f"Шаблон {datetime.now():%Y-%m-%d %H:%M:%S}"
        page.add_template(name)
        assert page.is_template_present(name), "Шаблон не создан"

    def test_user_creation(self, driver):
        page = self.main_page.go_to_users()
        email = f"test{datetime.now():%Y%m%d%H%M%S}@example.com"
        name = "Тест Пользователь"
        page.add_user(name, email)
        assert page.is_user_present(email), "Пользователь не создан"

    def test_role_creation(self, driver):
        page = self.main_page.go_to_roles()
        name = f"Роль {datetime.now():%Y-%m-%d %H:%M:%S}"
        page.add_role(name)
        assert page.is_role_present(name), "Роль не создана"