from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from project1.page.base_page import BasePage
from selenium import webdriver


btu0=(By.XPATH,'//*[@id="hamburger-container"]')
btu1=(By.XPATH,'//*[text()="商品管理"]')
btu2=(By.XPATH,'//*[text()="商品规格"]')
btu3=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[1]/span/button[1]')
name=(By.XPATH,'//form/div/div/div/div/div/div[1]/input')
btn1=(By.XPATH,'//*[text()="添加新规格"]')
gg=(By.XPATH,'//form/div/div[2]/div[1]/div/div/div/input')
ggz=(By.XPATH,'//form/div/div[2]/div[2]/div/div/div/input')
btn2=(By.XPATH,'//div[@class="mt10 el-col el-col-24"]/div[3]/button/span[text()="确定"]')
btn3=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[2]/div/div[3]/div/button[2]')


class GuigePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def click_btu0(self):
        self.click_el(btu0)
    def click_btu1(self):
        self.click_el(btu1)
    def click_btu2(self):
        self.click_el(btu2)

    def click_btu3(self):
        self.click_el(btu3)
    def set_name(self,value):
        self.set_el(name,value)

    def click_btn1(self):
        self.click_el(btn1)

    def set_gg(self, value):
        self.upload_el(gg,value)

    def set_ggz(self,value):
        self.set_el(ggz,value)

    def click_btn2(self):
        self.click_el(btu2)

    def click_btn3(self):
        self.click_el(btu3)

    def assert_text1(self):
        return self.text_el((By.XPATH,"//h2"))