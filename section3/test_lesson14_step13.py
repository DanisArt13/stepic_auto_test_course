from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegister(unittest.TestCase):
    
    def test_page1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys("Ivanov")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input2.send_keys("Ivan@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        self.assertEqual("Congratulations! You have successfully registered!", registration_result) 
        time.sleep(10)
        browser.quit()
        
        self.assertEqual("Congratulations! You have successfully registered!", registration_result) 
        
    def test_page2(self):
    
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys("Ivanov")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input2.send_keys("Ivan@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)
        time.sleep(10)
        browser.quit()
        
        

if __name__ == "__main__":
    unittest.main()
    