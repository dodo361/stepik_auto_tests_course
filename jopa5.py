import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу с сундуком
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    # Находим элемент-сундук и берем значение атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    # Отмечаем checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()
    
    # Нажимаем кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()