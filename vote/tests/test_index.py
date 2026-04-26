from pages.index import IndexPage
from pages.kontakty.KontaktyIndexPage import KontaktyIndexPage

def test_media(driver):
    index_page = IndexPage(driver)
    index_page.open()
    index_page.assert_h1()
    index_page.open_contacts()

    kontakty_index_page = KontaktyIndexPage(driver)
    kontakty_index_page.assert_h1()
