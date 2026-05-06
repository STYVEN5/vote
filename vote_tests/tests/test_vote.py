import pytest
from pages.vote_page import VotePage
import random

def test_title(driver):
    page = VotePage(driver)
    page.open()
    page.assert_title("Онлайн-голосования")

def test_invalid_code_shows_alert(driver):
    vote_page = VotePage(driver)
    vote_page.open()
    random_code = str(random.randint(100000, 999999))
    vote_page.enter_code(random_code)
    vote_page.click_submit()
    alert_text = vote_page.get_alert_text()
    assert any(word in alert_text.lower() for word in ["не найден", "неправильный", "ошибка", "не действителен"])

def test_empty_code_shows_alert(driver):
    page = VotePage(driver)
    page.open()
    assert page.is_code_input_present()
    assert page.is_submit_button_present()
    page.click_submit()
    alert_text = page.get_alert_text()
    expected_text = "Введите код приглашения"
    assert expected_text in alert_text