import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Вычисляем текст ссылки
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    
    # Открываем страницу с зашифрованной ссылкой
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    
    # Находим и кликаем по зашифрованной ссылке
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    
    # Заполняем форму
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()