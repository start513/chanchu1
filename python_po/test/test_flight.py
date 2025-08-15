from time import sleep

from selenium import webdriver
from page.login_page import LoginPage
from page.flight_page import FlightPage
import allure
@allure.feature("航班管理模块")
class TestFlightManage:
    @allure.story("testcase04")
    @allure.title("新增航班成功场景")
    def test_web_add_local_flight(self):
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
            flight_page=FlightPage(driver)
            flight_page.click_btn1()
        with allure.step("点击添加"):
            sleep(1)
            driver.get("http://localhost:8080/flight-manage-fixed.html")
            flight_page.click_btn2()
        with allure.step("输入航班号"):
            sleep(4)
            flight_page.set_num("zxc123")
        with allure.step("选择机型"):
            flight_page.click_sel1()
        with allure.step("选择出发机场"):
            flight_page.click_sel2()
        with allure.step("选择到达机场"):
            flight_page.click_sel3()
        with allure.step("输入出发时间"):
            flight_page.set_time1("2026")
        with allure.step("输入到达时间"):
            flight_page.set_time2("2027")
        with allure.step("点击确定"):
            flight_page.click_qd()

        with allure.step("断言结果"):
            assert "航班添加成功！" in flight_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(),"页面截图",allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/04.png")
        driver.quit()

    @allure.story("testcase05")
    @allure.title("修改航班成功场景")
    def test_web_add_local_flight(self):
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
            flight_page=FlightPage(driver)
            flight_page.click_btn1()
        with allure.step("点击编辑"):
            sleep(2)
            flight_page.click_bj()
        with allure.step("修改出发时间"):
            flight_page.set_time01("202601010101")
        with allure.step("修改到达时间"):
            flight_page.set_time02("202601020101")
        with allure.step("点击确定"):
            flight_page.click_qd2()

        with allure.step("断言结果"):
            assert "航班添加成功！" in flight_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(),"页面截图",allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/05.png")
        driver.quit()

    @allure.story("testcase06")
    @allure.title("修改航班成功场景")
    def test_web_add_local_flight(self):
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
            flight_page = FlightPage(driver)
            flight_page.click_btn1()
        with allure.step("点击编辑"):
            sleep(2)
            flight_page.click_bj2()
        with allure.step("修改出发时间"):
            flight_page.set_time001("202601010101")
        with allure.step("修改到达时间"):
            flight_page.set_time002("202601020101")
        with allure.step("点击确定"):
            flight_page.click_qd3()

        with allure.step("断言结果"):
            assert "航班添加成功！" in flight_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(), "页面截图", allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/06.png")
        driver.quit()
