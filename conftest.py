import pytest
from selenium import webdriver as selenium_wd
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://petfriends.skillfactory.ru"
USER = "flynn26@mail.ru"
PASSWORD = "789456123"


@pytest.fixture(scope="session")
def selenium_driver(request):
    s = Service(executable_path=GeckoDriverManager().install())
    firefox_options = Options()
    driver = selenium_wd.Firefox(service=s, options=firefox_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(BASE_URL+"/login")
    WDW(driver, 2).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(USER)
    driver.find_element(By.ID, "pass").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    yield driver
    driver.quit()
