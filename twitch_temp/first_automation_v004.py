import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
link = "https://twitch.tv"

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_window_size(1024, 768)
driver.get(link)
print('browser is open')

btn_cookie = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-a-target="consent-banner-accept"]')))
btn_cookie.click()

time.sleep(1)

btn_registration = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-selector="anon-user-menu__login-button"]')))
btn_registration.click()

time.sleep(1)

input_name = driver.find_element(By.CSS_SELECTOR, '#login-username')
input_name.send_keys(r'arazumtest2')

input_password = driver.find_element(By.CSS_SELECTOR, '#password-input')
input_password.send_keys(r'arazumtestTWI')

time.sleep(1)

input_enter = driver.find_element(By.CSS_SELECTOR, '[data-a-target="passport-login-button"]')
input_enter.click()
print('click Enter')

time.sleep(10)

driver.close()
print('close')
driver.quit()
print('quit. test OK')
