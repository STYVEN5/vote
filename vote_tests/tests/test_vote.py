import pytest
from pages.vote_page import VotePage
import random

def test_title(driver):
    page = VotePage(driver)
    page.open()
    page.assert_title("Онлайн-голосования")

def test_invalid_code_shows_alert(driver):
    """Попытка входа с неверным кодом → ожидаем ошибку"""
    vote_page = VotePage(driver)
    vote_page.open()
    
    # Генерируем случайный 6-значный код
    random_code = str(random.randint(100000, 999999))
    vote_page.enter_code(random_code)
    vote_page.click_submit()
    
    # Получаем текст alert (или ошибку на странице)
    alert_text = vote_page.get_alert_text()
    assert any(word in alert_text.lower() for word in ["не найден", "неправильный", "ошибка", "не действителен"]), \
        f"Неожиданный текст алерта: {alert_text}"

def test_empty_code_shows_alert(driver):
    """Проверяет, что при отправке пустого кода появляется alert с текстом 'Введите код приглашения'"""
    page = VotePage(driver)
    page.open()

    assert page.is_code_input_present(), "Поле ввода кода не найдено"
    assert page.is_submit_button_present(), "Кнопка 'Войти' не найдена"

    page.click_submit()

    alert_text = page.get_alert_text()
    expected_text = "Введите код приглашения"
    assert expected_text in alert_text, f"Ожидался текст '{expected_text}', получен '{alert_text}'"
