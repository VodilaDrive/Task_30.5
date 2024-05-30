import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Firefox()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()

def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('flynn26@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('789456123')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

def test_show_my_pets(driver):
    # Явное ожидания
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('flynn26@mail.ru')
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass')))
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('789456123')
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
    # Нажимаем на кнопку войти
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Переходим в раздел Мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем питомцев в разделе мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').text == "Мои питомцы"
    # Находим таблицу с питомцами
    driver.find_element(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    # Делаем скриншот
    driver.save_screenshot('allMyPets.jpeg')
