from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.driver.get("http://10.1.2.14:8080/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def click_el(self,path):
        self.driver.find_element(*path).click()
    def click_els(self,path,index):
        self.driver.find_elements(*path)[index].click()
    def set_els(self,path,index,value):
        self.driver.find_elements(*path)[index].send_keys(value)

    def set_el(self,path,value):
        self.driver.find_element(*path).clear()
        self.driver.find_element(*path).send_keys(value)
    def upload_el(self,path,value):
        self.driver.find_element(*path).send_keys(value)
    def text_el(self,path):
        return self.driver.find_element(*path).text

    def sw_frame(self,frame):
        self.driver.switch_to.frame(self.driver.find_element(*frame))
    def quit_frame(self):
        self.driver.switch_to.default_content()
