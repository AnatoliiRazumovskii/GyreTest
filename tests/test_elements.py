import time

from pages.page_base import BasePage
from pages.page_element import TextBoxPage


class TestElements:
    class TestTestBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(3)
            output_full_name, output_email, output_current_address, output_permanent_address = \
                text_box_page.check_filled_form()
            assert full_name == output_full_name, "full_name mistake"
            assert email == output_email, "email mistake"
            assert current_address == output_current_address, "current_address"
            assert permanent_address == output_permanent_address, "permanent_address"


# def test(driver):
#     page = BasePage(driver, 'https://twitch.tv')
#     page.open()
#     time.sleep(3)