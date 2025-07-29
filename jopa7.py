import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Прокручиваем страницу вниз до текстового поля
    answer_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer_field)
    
    # Вводим ответ
    answer_field.send_keys(y)
    
    # Отмечаем checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("arguments[0].click();", button)

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()