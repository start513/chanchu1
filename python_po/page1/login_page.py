from selenium.webdriver.common.by import By

from project1.page.base_page import BasePage
from selenium import webdriver


name=(By.XPATH,'//*[@id="username"]')
paw=(By.XPATH,'//*[@id="password"]')
but=(By.XPATH,'//*[@id="loginbutton"]')
dy1=(By.XPATH,'//h2')
dy2=(By.XPATH,'//form/div[2]/div/div[2]')
dy3=(By.XPATH,'//*[@id="breadcrumb-container"]/span/span/span[1]/span')



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def set_name(self,value):
        self.set_el(name, value)
    def set_paw(self,value):
        self.set_el(paw,value)

    def click_but(self):
        self.click_el(but)

    def assert_text1(self,ty):
        if ty==3:
            return self.text_el(dy1)
        elif ty==2:
            return self.text_el(dy2)
        else:
            return self.text_el(dy3)

