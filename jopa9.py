from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1. Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # 2. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # 3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # 4. Решить капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Получить результат
    print(browser.switch_to.alert.text.split()[-1])
    
finally:
    time.sleep(5)
    browser.quit()