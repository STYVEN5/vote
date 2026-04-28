import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from dotenv import load_dotenv
from pages.admin_login_page import AdminLoginPage

load_dotenv()

class TestAdminLogin:

    def test_admin_login_page_has_correct_title(self, driver):
        """Проверка заголовка страницы логина"""
        login_page = AdminLoginPage(driver)
        login_page.open()
        assert "Войдите в свою учетную запись" in driver.title, "Неверный заголовок страницы"

    def test_admin_login_invalid_credentials(self, driver):
        """Вход с неверными данными → сообщение об ошибке"""
        login_page = AdminLoginPage(driver)
        login_page.open()
        login_page.enter_email("wrong@example.com")
        login_page.enter_password("wrongpass")
        login_page.click_login()

        error_text = login_page.get_error_message()
        assert "некорректные данные" in error_text.lower(), \
            f"Ожидалась фраза 'некорректные данные', получено: {error_text}"