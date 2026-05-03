import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import time
from pages.setup_page import SetupPage

def test_reset_database(driver):
    setup_page = SetupPage(driver)
    setup_page.open()
    setup_page.click_reset_db()
    time.sleep(2)

def test_create_admin(driver):
    setup_page = SetupPage(driver)
    # Используем тот же driver, но чтобы быть уверенным, переоткроем страницу
    driver.get(SetupPage.URL)
    time.sleep(1)
    setup_page.click_create_admin()