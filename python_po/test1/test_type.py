from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from project1.page.login_page import LoginPage
from project1.page.type_page import TypePage
from selenium import webdriver
import allure
from datetime import datetime


@allure.feature("商品分类模块")
class TestLogin:
    @allure.story("testcase02")
    @allure.title("新增分类场景")
    def test_shangping_tpye(self):
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
        type_page=TypePage(driver)
        with allure.step("打开商品分类"):
            # type_page.click_btu0()
            type_page.click_btu1()
            type_page.click_btu2()
        with allure.step("点击新增"):
            type_page.click_btu3()
        with allure.step("输入名称"):
            type_page.set_name("66666")
        with allure.step("上传图片"):
            type_page.click_tupain()
            type_page.set_sc(r"C:\Users\ks\Desktop\666.png")
            type_page.click_tupain1()
            # driver.execute_script("window.scrollBy(0,1000);")
            driver.find_element(By.XPATH,"//main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label").send_keys(Keys.PAGE_DOWN)
            sleep(1)
            type_page.click_btu01()
        with allure.step("选择状态"):
            type_page.click_zt()
        with allure.step("输入排序"):
            type_page.set_px("2")
        # with allure.step("选择分类"):
        #     type_page.set_type("123456")
        with allure.step("点击确定"):
            type_page.click_qd()
        with allure.step("断言"):
            sleep(2)
            assert type_page.assert_text1()=="新增成功"
        allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'),allure.attachment_type.PNG)
        driver.get_screenshot_as_file(f"./screen/testcase01_{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}.png")
        driver.quit()

