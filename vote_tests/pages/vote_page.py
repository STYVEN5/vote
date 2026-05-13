from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VotePage:
    URL = "https://vote.susu.ru/"

    # Локаторы
    CODE_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_title(self) -> str:
        return self.driver.title

    def assert_title(self, expected_title: str = "Онлайн-голосования"):
        actual = self.get_title()
        assert actual == expected_title, f"Ожидался заголовок '{expected_title}', получен '{actual}'"

    # --- Форма входа ---
    def is_code_input_present(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.CODE_INPUT))
            return True
        except:
            return False

    def is_submit_button_present(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON))
            return True
        except:
            return False

    def click_submit(self):
        button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        button.click()

    def get_alert_text(self) -> str:
        """Получает текст всплывающего alert и закрывает его"""
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    # --- Методы для сегментов (оставлены для будущего) ---
    def get_segments(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-range]")))
        return self.driver.find_elements(By.CSS_SELECTOR, "[data-range]")

    def click_segment(self, index=0):
        segments = self.get_segments()
        assert len(segments) > index, f"Нет сегмента с индексом {index}"
        self.wait.until(EC.element_to_be_clickable(segments[index])).click()

    def enter_code(self, code: str):
        """Вводит код приглашения в поле"""
        input_element = self.wait.until(EC.presence_of_element_located(self.CODE_INPUT))
        input_element.clear()
        input_element.send_keys(code)