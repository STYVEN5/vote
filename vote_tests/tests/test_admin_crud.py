import pytest
import os
from pages.admin.login_page import AdminLoginPage
from pages.admin.main_page import AdminMainPage

class TestAdminCRUD:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        login_page = AdminLoginPage(driver).open()
        login_page.enter_email(os.getenv("ADMIN_EMAIL", "admin@laratest.susu.ru"))
        login_page.enter_password(os.getenv("ADMIN_PASSWORD", "R1j4rhnRZtC0bGi6"))
        login_page.click_login()
        login_page.wait.until(lambda d: "/admin/main" in d.current_url)
        self.main_page = AdminMainPage(driver)

    def test_advice_creation(self, driver):
        name = "Тестовый совет"
        
        print(f"\nCreating advice: {name}")
        index_page = self.main_page.go_to_advices()
        create_page = index_page.click_add_button()
        details_page = create_page.fill_name(name).save()
        
        print("Checking if on details page...")
        assert details_page.is_at_advice(name), f"Совет '{name}' не создан или не произошло перенаправление"
        
        # Создаем мероприятие
        event_create_page = details_page.click_add_event()
        event_name = "Тестовое мероприятие"
        event_details_page = event_create_page.fill_name(event_name).save()
        details_page = event_details_page.go_back_to_advice(name)
        assert details_page.is_at_advice(name), "Не вернулись на страницу совета после создания мероприятия"
        
        print("Checking admin link...")
        users_page = details_page.click_add_admin()
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(driver, 10).until(EC.url_contains("users"))
        assert "users" in driver.current_url, f"Ожидался переход в /admin/users, но текущий URL: {driver.current_url}"

    def test_poll_template_creation(self, driver):
        index_page = self.main_page.go_to_poll_templates()
        create_page = index_page.click_add_button()
        name = "Тестовый шаблон"
        details_page = create_page.fill_name(name).fill_options().save()
        assert details_page.is_template_present(name), f"Шаблон '{name}' не создан"

    def test_user_creation(self, driver):
        index_page = self.main_page.go_to_users()
        create_page = index_page.click_add_button()
        email = "testuser@example.com"
        name = "Тестовый пользователь"
        index_page = create_page.fill_name(name).fill_email(email).fill_password().save()
        assert index_page.is_user_present(email), f"Пользователь '{email}' не создан"

    def test_role_creation(self, driver):
        index_page = self.main_page.go_to_roles()
        create_page = index_page.click_add_button()
        name = "Тестовая роль"
        index_page = create_page.fill_name(name).fill_slug(name).save()
        assert index_page.is_role_present(name), f"Роль '{name}' не создана"