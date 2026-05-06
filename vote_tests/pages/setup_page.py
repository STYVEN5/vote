from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SetupPage:
    URL = "https://laratest.susu.ru/tests"

    # Локаторы кнопок (по значению атрибутов value)
    RESET_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][name='reset'][value='Сброс базы данных']")
    CREATE_ADMIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][name='create-admin'][value='Создание администратора']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Таймаут ожидания элементов (сек)

    def open(self):
        """Открывает страницу /tests"""
        self.driver.get(self.URL)

    def click_reset_db(self):
        """Находит кнопку сброса БД и кликает по ней (через JS для надёжности)."""
        reset_btn = self.wait.until(EC.element_to_be_clickable(self.RESET_BUTTON))
        self.driver.execute_script("arguments[0].click();", reset_btn)
        time.sleep(1)  # Небольшая пауза для применения сброса

    def click_create_admin(self):
        """Находит кнопку создания администратора и кликает по ней (через JS)."""
        admin_btn = self.wait.until(EC.element_to_be_clickable(self.CREATE_ADMIN_BUTTON))
        self.driver.execute_script("arguments[0].click();", admin_btn)
        time.sleep(1)  # Пауза для завершения операции