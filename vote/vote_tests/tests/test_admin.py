import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from dotenv import load_dotenv
from pages.admin_login_page import AdminLoginPage

load_dotenv()

class TestAdminLogin:
    def test_admin_login_page_has_correct_title(self, driver):
        login_page = AdminLoginPage(driver)
        login_page.open()
        assert "Войдите в свою учетную запись" in driver.title

    def test_admin_login_invalid_credentials(self, driver):
        login_page = AdminLoginPage(driver)
        login_page.open()
        login_page.enter_email("wrong@example.com")
        login_page.enter_password("wrongpass")
        login_page.click_login()
        error_text = login_page.get_error_message()
        assert "некорректные данные" in error_text.lower()

    def test_admin_login_success(self, driver):
        login_page = AdminLoginPage(driver)
        login_page.open()
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        assert login_page.is_login_successful()