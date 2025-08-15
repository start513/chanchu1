from time import sleep
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from project1.page.login_page import LoginPage
from project1.page.yunfei_page import YunfeiPage
from selenium import webdriver
import allure
from datetime import datetime


@allure.feature("运费模板模块")
class TestYunfei:
    @allure.story("testcase03")
    @allure.title("新增运费模板场景")
    def test_shangping_moban(self):
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
        yunfei_page=YunfeiPage(driver)
        with allure.step("打开运费模板"):
            # type_page.click_btu0()
            yunfei_page.click_btu1()
            yunfei_page.click_btu2()
        with allure.step("点击新增"):
            yunfei_page.click_btu3()
        with allure.step("输入名称"):
            yunfei_page.set_name("66666")
        # with allure.step("选择计费方式"):
        #     sleep(2)
        #     yunfei_page.click_jffs()
        with allure.step("添加配送区域"):
            sleep(1)
            yunfei_page.click_tjqy()
            sleep(1)
            yunfei_page.click_cs()
            sleep(1)
            yunfei_page.click_sq()
            sleep(1)
            yunfei_page.click_qd()

        with allure.step("点击确定"):
            yunfei_page.click_tj()
        with allure.step("断言"):
            sleep(2)
            assert yunfei_page.assert_text1()=="新增成功"
        allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),allure.attachment_type.PNG)
        driver.get_screenshot_as_file(f"./screen/testcase01_{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}.png")
        driver.quit()