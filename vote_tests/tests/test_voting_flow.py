import sys
import os
import random
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from dotenv import load_dotenv
from pages.admin.login_page import AdminLoginPage
from pages.admin.main_page import AdminMainPage
from pages.vote_page import VotePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

class TestVotingFlow:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        if not email or not password:
            pytest.skip("ADMIN_EMAIL или ADMIN_PASSWORD не заданы в .env")
        login_page = AdminLoginPage(driver).open()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        login_page.wait.until(lambda d: "/admin/main" in d.current_url)
        self.main_page = AdminMainPage(driver)

    def test_full_voting_cycle(self, driver):
        advices_page = self.main_page.go_to_advices()
        create_advice_page = advices_page.click_add_button()
        advice_name = f"Совет {random.randint(1000, 9999)}"
        advice_details = create_advice_page.fill_name(advice_name).save()
        assert advice_details.is_at_advice(advice_name), "Совет не создан"

        event_create = advice_details.click_add_event()
        event_name = f"Мероприятие {random.randint(1000, 9999)}"
        event_details = event_create.fill_name(event_name).save()

        start_button = (By.XPATH, "//button[.//span[text()='Начать']]")
        try:
            start_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start_button))
            ActionChains(driver).move_to_element(start_btn).click().perform()
        except TimeoutException:
            pytest.fail("Кнопка 'Начать' не найдена")

        try:
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(start_button))
        except TimeoutException:
            pass

        driver.refresh()
        WebDriverWait(driver, 3).until(lambda d: d.execute_script("return document.readyState") == "complete")

        add_participants_btn = (By.XPATH, "//a[contains(@href, '/members/generate')]")
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(add_participants_btn))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            ActionChains(driver).move_to_element(element).click().perform()
        except TimeoutException:
            pytest.fail("Кнопка 'Добавить участников' не найдена")

        count = random.randint(1, 5)
        count_input = (By.NAME, "amount")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(count_input)).send_keys(str(count))

        code_length_input = (By.NAME, "length")
        driver.find_element(*code_length_input).clear()
        driver.find_element(*code_length_input).send_keys("4")

        create_btn = (By.XPATH, "//button[@type='submit']")
        driver.find_element(*create_btn).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        code_cell_locator = (By.XPATH, "//table/tbody/tr[1]/td[1]")
        code_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(code_cell_locator))
        invite_code = code_element.text
        assert invite_code and len(invite_code) == 4, f"Неверный код: {invite_code}"

        
        site_url = "https://vote.susu.ru"
        driver.get(site_url)
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        vote_page = VotePage(driver)
        vote_page.enter_code(invite_code)
        vote_page.click_submit()
        WebDriverWait(driver, 10).until(lambda d: "голосование" in d.title.lower())
        assert "голосование" in driver.title.lower()