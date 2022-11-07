import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")   # function для открытия в SetUp и закрытия TD каждого теста (не класса, не модуля)
                                    # для обеспечения независимости теста
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(1024, 1044)
    yield driver  # как return (верни драйвер)
                # данная команда ждёт полной отработки алгоритма, в котором была использована, после чего идёт дальше
    driver.close()
    driver.quit()
