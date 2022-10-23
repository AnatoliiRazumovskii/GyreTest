import unittest
import pytest
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup

# отключение режима драйвера (для сайтов)
# подключаем опции
options = webdriver.ChromeOptions()

# отключение режима драйвера (для сайтов)
options.add_argument("--disable-blink-features=AutomationControlled")

link = "https://twitch.tv"
driver = webdriver.Chrome()
driver.set_window_size(1024, 768)
driver.get(link)
print('browser is open')
registration_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test"
                                                                                                    "-selector='anon"
                                                                                                    "-user"
                                                                                                    "-menu__login"
                                                                                                    "-button']")))
registration_btn.click()

time.sleep(2)


# class Test_Gyre(unittest.TestCase):
#     def test_registered_user(self):
#         self.assertEqual(driver.title, "Войти - Twitch")


# input_name = driver.find_element(By.ID, '[id="#login-username"]')
# input_name.send_keys('arazumtest2')
#
# input_password = driver.find_element(By.ID, '[id="#password-input"]')
# input_password.send_keys('arazumtestTWI')
#
# time.sleep(1)
# input_enter = driver.find_element(By.CSS_SELECTOR, '[data-a-target="passport-login-button"]')
# input_enter.click()

input_name = driver.find_element(By.CSS_SELECTOR, '#login-username')
# input_name = driver.find_element(By.XPATH, '//input[@id="login-username"]')
input_name.send_keys(r'arazumtest2')

# input_password = driver.find_element(By.XPATH, '//input[@aria-label="Введите свой пароль"]')  # ??? почему CSS_SELECTOR по тегу не раьотает
input_password = driver.find_element(By.CSS_SELECTOR, '#password-input')
input_password.send_keys(r'arazumtestTWI')
time.sleep(1)
input_enter = driver.find_element(By.CSS_SELECTOR, '[data-a-target="passport-login-button"]')
input_enter.click()

time.sleep(2)

driver.close()
driver.quit()
print('test OK')
