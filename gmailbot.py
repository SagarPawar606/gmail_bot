from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time


class Gmailbot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Firefox()   
    
    def login(self):
        driver = self.driver
        driver.get("https://www.gmail.com/")
                #will trhow assertion error if google is not found in title
        assert "Gmail" in driver.title
                #identifying elements from html page
        email_field = driver.find_element_by_xpath("//input[@name='identifier']")
        email_field.clear()

                #entering your emial
        email_field.send_keys(self.email)
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)
        nxt_btn = driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
        assert "No results found." not in driver.page_source
        nxt_btn.click()
        time.sleep(2)

                #entering your password
        password_field = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(2)
        nxt_btn = driver.find_element_by_xpath("//span[@class='CwaK9']")
        assert "No results found." not in driver.page_source
        nxt_btn.click()
      
with open('config.json','r') as data_file:
        data = json.load(data_file)
        email = data['email']
        password = data['pass']
        
obj = Gmailbot(email, password)
obj.login()
