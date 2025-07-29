from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    # Инициализируем браузер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Создаем временный файл для загрузки
    with open("testfile.txt", "w") as file:
        file.write("Это тестовый файл")  # Можно оставить пустым
    
    # Получаем абсолютный путь к файлу
    file_path = os.path.abspath("testfile.txt")
    
    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    
    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # Даем время скопировать код и удаляем временный файл
    time.sleep(30)
    browser.quit()
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")