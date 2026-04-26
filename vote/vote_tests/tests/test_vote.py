import pytest
from pages.vote_page import VotePage

def test_title(driver):
    page = VotePage(driver)
    page.open()
    page.assert_title("Онлайн-голосования")

@pytest.mark.xfail(reason="Сегменты появляются только после ввода кода, тестового кода пока нет")
def test_segments_exist(driver):
    page = VotePage(driver)
    page.open()
    segments = page.get_segments()
    assert len(segments) > 0

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
