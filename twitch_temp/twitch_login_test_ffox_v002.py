import unittest
import time
import pickle

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

class Test_Gyre (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.set_window_size (1024, 768) # self.driver.maximize_window() - весь экран

    def test_registered_user(self):
        link = "https://twitch.tv"
        # link = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html" #линк для проверки того, как нас видит система, как драйвер или как пользователя
        # link = "https://master.gyre.pages.dev"
        self.driver.get(link)
        # registration_btn = self.driver.find_element(By.CSS_SELECTOR, ".page-header__sign-up-btn")

        registration_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-header__sign-up-btn")))
        registration_btn.click()

        registration_by_Twitch = self.driver.find_element(By.XPATH, "//a[@class='sign-up-modal__sign-up-with-twitch-button']")
        registration_by_Twitch.click()

        self.assertEqual(self.driver.title, "Войти - Twitch")


        input_name = self.driver.find_element(By.XPATH, '//input[@id="login-username"]')
        input_name.send_keys(r'arazumtest2')

        input_password = self.driver.find_element(By.XPATH, '//input[@aria-label="Введите свой пароль"]')
        input_password.send_keys(r'arazumtestTWI')
        time.sleep(1)
        input_enter = self.driver.find_element(By.XPATH, '//div[@data-a-target="tw-core-button-label-text"]')
        input_enter.click()

        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()