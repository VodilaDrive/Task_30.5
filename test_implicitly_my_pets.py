import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Firefox()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()

def test_implicitly_wait_my_pets(driver):
    # Неявное ожидание
    driver.implicitly_wait(5)
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('flynn26@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('789456123')
    # Нажимаем на кнопку войти
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Неявное ожидание
    driver.implicitly_wait(5)
    # Переходим в раздел мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    # Проверяем, что перешли в раздел Мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').text == "Мои питомцы"

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    # Проверяем данные питомцев
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0