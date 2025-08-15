from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/login-fixed.html")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def click_el(self,path):
        self.driver.find_element(*path).click()

    def set_el(self,path,value):
        self.driver.find_element(*path).clear()
        self.driver.find_element(*path).send_keys(value)

    def select_el(self,path,index):
        select=Select(self.driver.find_element(*path))
        select.select_by_index(index)
    def text_el(self,path):
        return self.driver.find_element(*path).text

    def text_alert(self):
        return self.driver.switch_to.alert.text
