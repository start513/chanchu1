from time import sleep
import pytest
from project1.page.login_page import LoginPage
from selenium import webdriver
import allure
from datetime import datetime


@allure.feature("登录模块")
class TestLogin:
    @allure.story("testcase01")
    @allure.title("登录成功场景")
    @pytest.mark.parametrize("user,paw,ass,ty",[
        ("admin","123456","首页",1),
        ("admin","","首页",1),
        ("admin","12345","用户名或密码错误",3)
    ])
    def test_login_success(self,user,paw,ass,ty):
        with allure.step("打开浏览器"):
            driver=webdriver.Chrome()
            login_page=LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name(user)
        with allure.step("输入密码"):
            login_page.set_paw(paw)
        with allure.step("点击登录"):
            login_page.click_but()
        with allure.step("断言"):
            sleep(2)
            assert login_page.assert_text1(ty)==ass
        allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),allure.attachment_type.PNG)
        driver.get_screenshot_as_file(f"./screen/testcase01_{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}.png")
        driver.quit()
