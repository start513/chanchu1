from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from project1.page.base_page import BasePage
from selenium import webdriver


btu0=(By.XPATH,'//*[@id="hamburger-container"]')
btu1=(By.XPATH,'//*[text()="商品管理"]')
btu2=(By.XPATH,'//*[text()="运费模板"]')
btu3=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[1]/span/button[1]')
name=(By.XPATH,'//form/div[1]/div/div/div/div/input')
sel1=(By.XPATH,'//div[@class="el-radio-group radio"]/label[2]/span[1]/input[@value=2]')
btn01=(By.XPATH,'//*[text()="单独添加配送区域"]')
sel2=(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[19]/div/label")
sel3=(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[19]/div/div/div/div[2]/label[3]/span[2]")
btn02=(By.XPATH,'//div[@class="el-dialog__footer"]/div/button/span[text()="确定"]')

input1=(By.XPATH,"//form/div[5]/div/div/div/div/div/input")
btn03=(By.XPATH,"//*[text()='立即提交']")




class YunfeiPage(BasePage):
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

    def click_jffs(self):
        self.click_el(sel1)



    def click_tjqy(self):
        self.click_el(btn01)

    def click_cs(self):
        self.click_el(sel2)
    def click_sq(self):
        self.click_el(sel3)

    def click_qd(self):
        self.click_el(btn02)

    def set_px(self, value):
        self.set_el(input1, value)
    def click_tj(self):
        self.click_el(btn03)
    def assert_text1(self):
        return self.text_el((By.XPATH,"//h2"))
