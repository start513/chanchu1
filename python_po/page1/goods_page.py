from time import sleep
import pytest
from selenium import webdriver
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from project1.page.base_page import BasePage
btu0=(By.XPATH,'//*[@id="hamburger-container"]')
btu1=(By.XPATH,'//*[text()="商品管理"]')
btu2=(By.XPATH,'//*[text()="管理商品"]')
btu3=(By.XPATH,'//*[@id="pane-first"]/div/div[1]/div[4]/button[1]')

name=(By.XPATH,'//form/div[1]/div[1]/div/div/div[1]/input')
t1=(By.CSS_SELECTOR,'form > div:nth-child(1) > div:nth-child(2)  div  div  div:nth-of-type(1)  div > input')
t111=(By.XPATH,'//form/div[1]/div[2]/div/div/div/div/input')
t2=(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li/span')
t3=(By.XPATH,'//form/div[1]/div[3]/div/div/div/input')
t4=(By.XPATH,'//section/div[1]/div/div/form/div[1]/div[4]/div/div/div[1]/input')
t5=(By.XPATH,'//form/div[1]/div[6]/div/div/div/div[1]')
t7=(By.XPATH,'//section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label')

t9=(By.CSS_SELECTOR,".el-button--primary")
t10=(By.XPATH,'//form/div[1]/div[7]/div/div/div/div[1]')
t11=(By.XPATH,'//label[@class="el-checkbox material-name"]')
# (By.XPATH,'//label[@class="el-checkbox material-name"]')
t12=(By.XPATH,'//button[@class="el-button el-button--primary el-button--small"]')
t13=(By.XPATH,'//table/tbody/tr/td[5]/div/div/input')
# t13=(By.XPATH,'//table/tbody/tr/td[5]/div/div/input')
t14=(By.XPATH,'//form/div[1]/div[11]/div/div/div/div/div[1]/span')
t15=(By.XPATH,'//span[text()="默认全国运费模板"]')
t16=(By.XPATH,'//*[@id="ueditor_0"]')
t17=(By.XPATH,'/html/body/p')
t18=(By.XPATH,'//section/div[1]/div/div/form/div[4]/div/button')






class GoodsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_btu0(self):
        self.click_el(btu0)

    def click_btu1(self):
        self.click_el(btu1)

    def click_btu2(self):
        self.click_el(btu2)
    def click_btu3(self):
        self.click_el(btu3)
    def set_spmc(self,value):
        self.set_el(name,value)

    def click_spfl(self):
        self.click_el(t1)

    def click_spfl1(self):
        self.click_el(t2)

    def set_gjz(self, value):
        self.set_el(t3, value)
    def set_dw(self, value):
        self.set_el(t4, value)


    def click_fmt(self):
        self.click_el(t5)

    def click_down(self):
        self.click_el(t7)
        sleep(1)
        self.driver.execute_script("window.scrollBy(0, 450);")
        sleep(1)
        self.set_el(t7,Keys.PAGE_DOWN)
    def click_sc(self,value):
        self.set_els(t9,4,value)
    def click_qd(self):
        self.click_el(t9)

    def click_fmt1(self):
        self.click_el(t10)
    def click_xz1(self):
        self.click_el(t11)
        self.set_el(t11,Keys.PAGE_DOWN)

    def click_qd1(self):
        self.click_el(t12)

    def set_kc(self, value):
        self.set_el(t13, value)

    def click_xzmb(self):
        self.click_el(t14)
        sleep(3)
        self.click_el(t15)
        self.driver.execute_script("window.scrollBy(0, 450);")

    def set_xq(self, value):
        self.sw_frame(t16)
        self.set_el(t17,value)
        self.quit_frame()
        self.driver.execute_script("window.scrollBy(0, 450);")
    def click_qd3(self):
        self.click_el(t18)
    def assert_text1(self):
        return self.text_el((By.CSS_SELECTOR,".el-message__content"))
