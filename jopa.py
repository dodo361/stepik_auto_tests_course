from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = None  # Инициализируем переменную заранее

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим все текстовые поля
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    
    # Заполняем поля
    for element in elements:
        element.send_keys("Data")
    
    # Находим и кликаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Закрываем браузер, если он был открыт
    
    time.sleep(30)  # Даем время скопировать код
    browser.quit()