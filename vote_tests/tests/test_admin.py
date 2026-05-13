import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from dotenv import load_dotenv
from pages.admin.login_page import AdminLoginPage
from pages.admin.main_page import AdminMainPage

load_dotenv()

class TestAdminLogin:

    def test_admin_login_page_has_correct_title(self, driver):
        login_page = AdminLoginPage(driver).open()
        assert "Войдите в свою учетную запись" in driver.title

    def test_admin_login_invalid_credentials(self, driver):
        login_page = AdminLoginPage(driver).open()
        login_page.enter_email("wrong@example.com")
        login_page.enter_password("wrongpass")
        login_page.click_login()
        error_text = login_page.get_error_message()
        assert "некорректные данные" in error_text.lower()

    def test_admin_login_success(self, driver):
        login_page = AdminLoginPage(driver).open()
        login_page.enter_email(os.getenv("ADMIN_EMAIL", "admin@laratest.susu.ru"))
        login_page.enter_password(os.getenv("ADMIN_PASSWORD", "R1j4rhnRZtC0bGi6"))
        login_page.click_login()
        # Ждём смены URL
        login_page.wait.until(lambda d: "/admin/main" in d.current_url or "/admin" in d.current_url)
        assert "admin" in driver.current_url