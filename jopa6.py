from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")  # Можно заменить на selects2.html
    
    # Находим числа и вычисляем их сумму
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    total = str(int(num1) + int(num2))
    
    # Выбираем значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total)  # Ищем по значению
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()