import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)
    
    # Отмечаем checkbox
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robot_checkbox.click()
    
    # Выбираем radiobutton
    robots_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robots_rule.click()
    
    # Нажимаем Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()