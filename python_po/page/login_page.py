from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

name=(By.XPATH,'//*[@id="username"]')
paw=(By.XPATH,'//*[@id="password"]')
btn=(By.XPATH,'//*[@id="loginBtn"]')
text=(By.XPATH,'//*[@id="systemStatus"]/div')

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_name(self,value):
        self.set_el(name,value)

    def set_paw(self,value):
        self.set_el(paw,value)

    def click_login(self):
        self.click_el(btn)

    def text_dy(self):
        return self.text_el(text)