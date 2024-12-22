from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 300
shopping_time = time.time() + 5

while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()
    money = driver.find_element(By.ID, value="money")
    if time.time() > shopping_time:
        cursor_info = driver.find_element(By.CSS_SELECTOR, value = "#buyCursor b")
        cursor_price = int(cursor_info.text.split("-")[1])

        grandma_info = driver.find_element(By.CSS_SELECTOR, value = "#buyGrandma b")
        grandma_price = int(grandma_info.text.split("-")[1])

        factory_info = driver.find_element(By.CSS_SELECTOR, value = "#buyFactory b")
        factory_price = int(factory_info.text.split("-")[1])

        if int(money.text) > factory_price:
            factory = driver.find_element(By.ID, value = "buyFactory")
            factory.click()
        elif int(money.text) > grandma_price:
            grandma = driver.find_element(By.ID, value = "buyGrandma")
            grandma.click()
        elif int(money.text) > cursor_price:
            cursor = driver.find_element(By.ID, value = "buyCursor")
            cursor.click()
    
    if time.time() > timeout:
        break


driver.quit()