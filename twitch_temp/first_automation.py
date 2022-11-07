from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# отключение режима драйвера (для сайтов)
# подключаем опции
options = webdriver.ChromeOptions()

# отключение режима драйвера (для сайтов)
# для версий Хром до 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# отключение режима драйвера (для сайтов)
# для версий Хром новее, чем 79.0.3945.16
options.add_argument("--disable-blink-features=AutomationControlled")

# link = "https://gyre.tv/find-collab"
link = "https://forum.il2sturmovik.ru/"
browser = webdriver.Chrome()
browser.get(link)
print('browser is open')
time.sleep(2)

# получение куки
# pickle.dump(browser.get_cookies(), open("cook_gyre_il3_del", "wb"))
#
# # загрузка куки
# for cookie in pickle.load(open("cook_gyre_il3_del", "rb")):
#     browser.add_cookie(cookie)
# print('cookies loaded')
# time.sleep(3)
# browser.refresh()
# time.sleep(3)


#авторизация кнопками. начало. поиск и нажатие кнопки
# browser.pres #пока лишнее

# sign_up_button = browser.find_element(By.CSS_SELECTOR, '.sign-up-btn')
# print("Text is: " + sign_up_button.text)
# assert1check = sign_up_button.text == 'регистрация'
# assert assert1check, f'Sign Up text wrong {sign_up_button.text}'
#
# search_string = browser.find_element(By.ID, 'find-by-name-input')
# search_string.send_keys('arazum')
# print('set value to arazum')

time.sleep(2)

browser.quit()
print('test OK')