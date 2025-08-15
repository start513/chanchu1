from time import sleep

from selenium import webdriver
from page.login_page import LoginPage
from page.boarding_pass_page import PassPage
import allure
@allure.feature("登机牌管理模块")
class TestBoardingPassManage:
    @allure.story("testcase05")
    @allure.title("申请登机牌成功场景")
    def test_web_boarding_pass_apply(self):
        with allure.step("打开浏览器"):
            driver=webdriver.Chrome()
            login_page=LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("admin")
        with allure.step("输入密码"):
            login_page.set_paw("123456")
        with allure.step("点击登录"):
            login_page.click_login()
            sleep(3)
        with allure.step("进入管理"):
            pass_page=PassPage(driver)
            pass_page.click_btn1()
        with allure.step("点击添加"):
            sleep(4)
            pass_page.click_btn2()
        with allure.step("输入名字"):
            pass_page.set_name("zxc123")
        with allure.step("选择航班号"):
            pass_page.click_sel1()
        with allure.step("输入座位号"):
            pass_page.set_name1("zxc123")
        with allure.step("输入登机口"):
            pass_page.set_name2("zxc123")
        with allure.step("输入登机时间"):
            pass_page.set_time1("00202610101010")
        with allure.step("输入行李牌号"):
            pass_page.set_name3("zxc123")
        with allure.step("点击申请登机牌"):
            pass_page.click_qd()
        with allure.step("断言结果"):
            assert "登机牌申请成功！" in pass_page.text_dy()
            allure.attach(driver.get_screenshot_as_png(),"页面截图",allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/07.png")
        driver.quit()


    @allure.story("testcase05")
    @allure.title("申请登机牌成功场景")
    def test_web_boarding_pass_apply(self):
        with allure.step("打开浏览器"):
            driver = webdriver.Chrome()
            login_page = LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("admin")
        with allure.step("输入密码"):
            login_page.set_paw("123456")
        with allure.step("点击登录"):
            login_page.click_login()
            sleep(3)
        with allure.step("进入管理"):
            pass_page = PassPage(driver)
            pass_page.click_btn1()
        with allure.step("点击取消"):
            sleep(4)
            pass_page.click_qx()
        with allure.step("断言结果"):
            assert "登机牌取消成功！" in pass_page.text_dy()
            allure.attach(driver.get_screenshot_as_png(), "页面截图", allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/07.png")
        driver.quit()