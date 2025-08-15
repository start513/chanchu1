from time import sleep
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from project1.page.login_page import LoginPage
from project1.page.goods_page import GoodsPage
from selenium import webdriver
import allure
from datetime import datetime


@allure.feature("商品新增模块")
class TestGoods:
    @pytest.mark.parametrize("path",[(r"C:\Users\ks\Pictures\eight.png")])
    @allure.title("商品新增场景")
    @allure.story("testcase5")
    def test_shangping_xinzeng(self,path):
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
        goods_page=GoodsPage(driver)
        with allure.step("打开运费模板"):
            goods_page.click_btu1()
        with allure.step("打开商品管理"):
            goods_page.click_btu2()

        with allure.step("点击新增"):
            goods_page.click_btu3()
        with allure.step("输入商品名称"):
            goods_page.set_spmc("7777")
        with allure.step("选择商品分类"):

            sleep(5)
            goods_page.click_spfl()
            goods_page.click_spfl1()
        with allure.step("输入关键字"):
            goods_page.set_gjz("555")

        with allure.step("输入单位"):
            goods_page.set_dw("666")
        # with allure.step("选择商品封面图"):
        #
        #     goods_page.click_fmt()
        #     goods_page.click_sc(path)
        #     goods_page.click_down()
        #     goods_page.click_qd()
        # with allure.step("选择商品轮播图"):
        #     goods_page.click_fmt1()
        #     goods_page.click_xz1()
        #     goods_page.click_qd1()
        with allure.step("输入库存"):
            goods_page.set_kc("999")
        with allure.step("选择运费模板"):

            goods_page.click_xzmb()
        with allure.step("输入商品详情"):
            goods_page.set_xq("1111")
        with allure.step("点击确认"):
            goods_page.click_qd3()
        with allure.step("断言"):
            sleep(1)
            assert goods_page.assert_text1()=="请填写完整商品信息！"
        allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),allure.attachment_type.PNG)
        driver.get_screenshot_as_file(f"./screen/testcase01_{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}.png")
        driver.quit()