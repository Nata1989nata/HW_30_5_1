import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_my_pets(driver):
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('tartaletka1989@mail.ru')
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass')))
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('852456852456')
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Явное ожидание
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a')))
    # Переходим в раздел Мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a').click()
    # Проверяем таблицу всех питомцев в разделе Мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a').text == 'Мои питомцы'
    # Делаем скриншот
    driver.save_screenshot('allMyPets.png')


def test_implicitly_wait_my_pets(driver):
    # НЕявное ожидание
    driver.implicitly_wait(10)
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('tartaletka1989@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('852456852456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем что главная страница с питомцами открыта верно
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # НЕявное ожидание
    driver.implicitly_wait(10)
    # Переходим в раздел Мои питомцы
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a').click()
    # Проверяем таблицу всех питомцев в разделе Мои питомцы
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a').text == 'Мои питомцы'

    # Делаем скриншот
    driver.save_screenshot('implicitly_wait_my_pets.png')
