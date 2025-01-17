from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def cal_x(x):
    return math.log(abs(12*math.sin(x)))


link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
x_value = str(cal_x(int(x)))

x_input = browser.find_element(By.ID, "answer")
x_input.send_keys(x_value)

button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button2.click()

time.sleep(20)

browser.quit()