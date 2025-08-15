from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


btn1=(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/a')
btn2=(By.CSS_SELECTOR,".mb-0 + div  button:nth-child(1) i")
num=(By.XPATH,'//*[@id="flightNumber"]')
select1=(By.XPATH,'//*[@id="aircraft"]')
select2=(By.XPATH,'//*[@id="departureAirport"]')
select3=(By.XPATH,'//*[@id="arrivalAirport"]')
time1=(By.XPATH,'//*[@id="departureTime"]')
time2=(By.XPATH,'//*[@id="arrivalTime"]')
qd=(By.XPATH,'//*[@id="addFlightModal"]/div/div/div[3]/button[2]')
text=(By.XPATH,'//*[@id="systemStatus"]/div')

btn01=(By.CSS_SELECTOR,'#flightTableBody tr:nth-child(1) td:nth-child(9) button')
time01=(By.XPATH,'//*[@id="editDepartureTime"]')
time02=(By.XPATH,'//*[@id="editArrivalTime"]')
qd2=(By.XPATH,'//*[@id="editFlightModal"]/div/div/div[3]/button[2]')

bj=(By.XPATH,'//*[@id="flightTableBody"]/tr[1]/td[9]/button')
time001=(By.XPATH,'//*[@id="editDepartureTime"]')
time002=(By.XPATH,'//*[@id="editArrivalTime"]')
qd3=(By.XPATH,'//*[@id="editFlightModal"]/div/div/div[3]/button[2]')


class FlightPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    def click_btn1(self):
        self.click_el(btn1)

    def click_btn2(self):
        self.click_el(btn2)

    def set_num(self,value):
        self.set_el(num,value)
    def click_sel1(self):
        self.select_el(select1,2)
    def click_sel2(self):
        self.select_el(select2,2)
    def click_sel3(self):
        self.select_el(select3,3)

    def set_time1(self,value):
        self.set_el(time1,value)
    def set_time2(self,value):
        self.set_el(time2,value)
    def click_qd(self):
        self.click_el(qd)
    def click_bj(self):
        self.click_el(btn01)

    def click_qd2(self):
        self.click_el(qd2)

    def set_time01(self,value):
        self.set_el(time01,value)
    def set_time02(self,value):
        self.set_el(time02,value)
    def click_bj2(self):
        self.click_el(bj)
    def set_time001(self,value):
        self.set_el(time001,value)
    def set_time002(self,value):
        self.set_el(time002,value)

    def click_qd3(self):
        self.click_el(qd3)



    def text_dy(self):
        return self.text_alert()