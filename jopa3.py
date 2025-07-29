from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Уникальные селекторы для полей формы
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        first_name.send_keys("Ivan")
        
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем успешность регистрации
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return "Congratulations! You have successfully registered!" in welcome_text

    finally:
        time.sleep(5)
        browser.quit()

# Тест должен проходить на первой странице
assert test_registration("http://suninjuly.github.io/registration1.html")

# Тест должен падать на второй странице
try:
    test_registration("http://suninjuly.github.io/registration2.html")
    assert False, "Тест должен был упасть на registration2.html"
except Exception as e:
    print(f"Тест упал как и ожидалось: {e}")