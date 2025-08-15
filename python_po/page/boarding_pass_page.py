from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


btn1=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/a')
# btn2=(By.CSS_SELECTOR,".mb-0 + div  button:nth-child(1) i")
btn2=(By.ID,'id_6')
name=(By.XPATH,'//*[@id="passengerName"]')
select1=(By.XPATH,'//*[@id="flightNumber"]')
select2=(By.XPATH,'//*[@id="seatNumber"]')
select3=(By.XPATH,'//*[@id="gate"]')
time1=(By.XPATH,'//*[@id="boardingTime"]')
select4=(By.XPATH,'//*[@id="luggageTag"]')
qd=(By.XPATH,'//*[@id="applyBoardingPassModal"]/div/div/div[3]/button[2]')
qx=(By.XPATH,'//*[@id="boardingPassTableBody"]/tr[1]/td[9]/button')
text=(By.XPATH,'//*[@id="systemStatus"]/div')

class PassPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver=webdriver.Chrome()
    def click_btn1(self):
        self.click_el(btn1)

    def click_btn2(self):
        self.click_el(btn2)

    def set_name(self,value):
        self.set_el(name,value)
    def click_sel1(self):
        self.select_el(select1,2)
    def set_name1(self,value):
        self.set_el(select2,value)
    def set_name2(self,value):
        self.set_el(select3,value)
    def set_time1(self,value):
        self.set_el(time1,value)
    def set_name3(self,value):
        self.set_el(select4,value)
    def click_qd(self):
        self.click_el(qd)
    def click_qx(self):
        self.click_el(qx)
        self.driver.switch_to.alert.accept()
    def text_dy(self):
        return self.text_alert()