from time import sleep
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from project1.page.login_page import LoginPage
from project1.page.guige_page import GuigePage
from selenium import webdriver
import allure
from datetime import datetime


@allure.feature("商品规格模块")
class TestGuige:
    @allure.story("testcase03")
    @allure.title("新增规格场景")
    def test_shangping_guige(self):
        with allure.step("打开浏览器"):
            driver=webdriver.Chrome()
            login_page=LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("admin")
        with allure.step("输入密码"):
            login_page.set_paw("123456")
        with allure.step("点击登录"):
            sleep(1)
            login_page.click_but()
            sleep(1)
        guige_page=GuigePage(driver)
        with allure.step("打开商品分类"):
            # type_page.click_btu0()
            guige_page.click_btu1()
            guige_page.click_btu2()
        with allure.step("点击新增"):
            guige_page.click_btu3()
        with allure.step("输入名称"):
            guige_page.set_name("66666")
        with allure.step("添加规格"):
            sleep(1)
            guige_page.click_btn1()
            guige_page.set_gg("金属")
            guige_page.set_ggz("111")
            sleep(2)
            # guige_page.click_btn2()

        with allure.step("点击确定"):
            guige_page.click_btn2()
        with allure.step("断言"):
            sleep(2)
            assert guige_page.assert_text1()=="新增成功"
        allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),allure.attachment_type.PNG)
        driver.get_screenshot_as_file(f"./screen/testcase01_{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}.png")
        driver.quit()