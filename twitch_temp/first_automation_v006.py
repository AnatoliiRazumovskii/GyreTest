import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Отключение режима видимости драйвера (для сайтов). Указываем опцию отсюда https://peter.sh/experiments/chromium-command-line-switches/
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")


link = "https://twitch.tv"
# link = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html" #линк для проверки того, как нас видит система, как драйвер или как пользователя  # ссылка проверки состояния браузера


class Test_Twitch (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  # Подключаем опцию (ChromeDriverManager().install(), options=options)
        self.driver.set_window_size(1024, 768)

    def test_registered_user(self):
        self.driver.get(link)

        print('browser is open')

        driverwait = WebDriverWait(self.driver, 2)

        try:
            btn_cookie = driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-a-target="consent-banner-accept"]')), "екшфд ьып")
            btn_cookie.click()

        except TimeoutException as a:
            print("No Cookie banner")
            print(a.msg)
        # except Exception as e:
        #     print("No Cookie banner")

        time.sleep(1)

        btn_registration = driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-selector="anon-user-menu__login-button"]')))
        btn_registration.click()

        time.sleep(1)

        input_name = self.driver.find_element(By.CSS_SELECTOR, '#login-username')
        input_name.send_keys(r'arazumtest2')

        input_password = self.driver.find_element(By.CSS_SELECTOR, '#password-input')
        input_password.send_keys(r'arazumtestTWI')

        time.sleep(1)

        btn_enter = self.driver.find_element(By.CSS_SELECTOR, '[data-a-target="passport-login-button"]')
        btn_enter.click()
        print('click Enter')

        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.close()
        print('close')
        self.driver.quit()
        print('quit. test OK')


if __name__ == '__main__':
    unittest.main()
