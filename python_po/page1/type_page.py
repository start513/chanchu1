from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from project1.page.base_page import BasePage
from selenium import webdriver


btu0=(By.XPATH,'//*[@id="hamburger-container"]')
btu1=(By.XPATH,'//*[text()="商品管理"]')
btu2=(By.XPATH,'//*[text()="商品分类"]')
btu3=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[1]/div[2]/span/button[1]')
name=(By.XPATH,'//form/div[1]/div/div/input')
tupian=(By.XPATH,'//form/div[2]/div/div/div[1]')
sc=(By.XPATH,"//main/div/div[1]/div/div/div[2]/div/div/input")
tupian1=(By.XPATH,"//main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label/span[1]/span")
btu01=(By.CSS_SELECTOR,'body > div:nth-child(8) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small')
sel=(By.XPATH,"//form/div[3]/div/div/label[2]")
px=(By.XPATH,"//form/div[4]/div/div/input")
input1=(By.XPATH,"//form/div[5]/div/div/div[1]/div[1]/div[3]/input")
btu02=(By.XPATH,"//*[text()='确认']")




class TypePage(BasePage):
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

    def click_tupain(self):
        self.click_el(tupian)

    def set_sc(self, value):
        self.upload_el(sc,value)

    def click_tupain1(self):
        self.click_el(tupian1)

    def click_btu01(self):
        self.click_el(btu01)
    def click_zt(self):
        self.click_el(sel)

    def set_px(self,value):
        self.set_el(px,value)

    def set_type(self,value):
        self.set_el(input1,value)
        self.set_el(input1,Keys.ARROW_UP)
        sleep(1)
        self.set_el((By.XPATH,"//form/div[5]/label"),Keys.ENTER)

    def click_qd(self):
        self.click_el(btu02)

    def assert_text1(self):
        return self.text_el((By.XPATH,"//h2"))
