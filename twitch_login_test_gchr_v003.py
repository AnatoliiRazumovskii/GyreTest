import pytest
import unittest
import time
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()

# отключение режима драйвера (для сайтов)
options.add_argument("--disable-blink-features=AutomationControlled")


class Test_Gyre (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) # далее опция загрузки 1, без обмана. = webdriver.Chrome(ChromeDriverManager().install()) и опция загрузки 2, с обманом. = webdriver.Chrome(ChromeDriverManager().install(), options=options))
        self.driver.set_window_size (1024, 768)

    def test_registered_user(self):
        link = "https://twitch.tv"
        self.driver.get(link)
        registration_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test-selector='anon-user-menu__login-button']")))
        registration_btn.click()

        self.assertEqual(self.driver.title, "Войти - Twitch")
        # input_name = self.driver.find_element(By.XPATH, '//input[@id="login-username"]')
        input_name = self.driver.find_element(By.CSS_SELECTOR, "#login-username")
        input_name.send_keys(r'arazumtest2')

        input_password = self.driver.find_element(By.CSS_SELECTOR, "#password-input")
        input_password.send_keys(r'arazumtestTWI')
        time.sleep(1)
        input_enter = self.driver.find_element(By.CSS_SELECTOR, '[data-a-target="passport-login-button"]')
        input_enter.click()

        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()