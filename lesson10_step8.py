from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)


price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button1.click()

x = browser.find_element(By.ID, "input_value").text
x_value = str(calc(int(x)))

x_input = browser.find_element(By.ID, "answer")
x_input.send_keys(x_value)

button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(5)
browser.quit()