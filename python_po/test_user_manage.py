import csv
from time import sleep
import ddt
import pytest
from selenium import webdriver
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime

def read():
    with open(r"C:\Users\ks\Desktop\data.csv","r",encoding="utf-8") as f:
        data=csv.reader(f)
        next(data)
        list=[]
        for i in data:
            list.append(tuple(i))
        return list


@allure.feature("用户管理模块")
@ddt.ddt
class TestUserAdd:
    # @pytest.mark.parametrize("username,password",[(14300000011,123456),(14300000012,123456),(14300000013,123456),(14300010004,123456),(14300010005,123456),(14300100006,123456),(14300000107,123456),(14300000108,123456),(14300010009,123456),(14300100010,123456),])
    @pytest.mark.parametrize("username,password",read())
    @allure.title("用户新增场景")
    @allure.story("testcase2")
    # @ddt.data(*[(14300000011,123456),(14300000012,123456)])
    def test_web_user_add(self,username,password):
        with allure.step("创建浏览器,打开网址"):
            driver=webdriver.Chrome()
            driver.get("http://10.1.2.14:8080/#/login")
            driver.implicitly_wait(10)
        with allure.step("清空并输入账号"):
            driver.find_element(By.XPATH,'//*[@id="username"]').clear()
            driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("admin")
        with allure.step("清空并输入密码"):
            driver.find_element(By.XPATH,'//*[@id="password"]').clear()
            driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("123456")
        with allure.step("点击登录按钮"):
            driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
        with allure.step("打开用户管理"):
            driver.get("http://10.1.2.14:8080/#/system/user")
        with allure.step("点击新增"):
            driver.find_element(By.XPATH,'//section/div[1]/div/div[2]/div[1]/div[2]/span/button[1]/span').click()
        with allure.step("输入用户名"):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(username)
        with allure.step("输入手机号"):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[2]/div/div[1]/input').send_keys(username)
        with allure.step("输入昵称"):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[3]/div/div[1]/input').send_keys(username)
        with allure.step("输入邮箱"):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[4]/div/div[1]/input').send_keys(f"{username}@163.com")
        with allure.step("选择部门"):
            driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys("研发部")
            driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ENTER)
        with (allure.step("选择岗位")):
            driver.find_element(By.XPATH,'//form/div[6]/div/div/div/input').click()
            driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        with allure.step("选择角色"):
            driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div').click()
            sleep(0.5)
            driver.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
            driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div').click()
        with allure.step("点击确认"):
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[2]/span').click()
        with allure.step("断言结果"):
            allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),allure.attachment_type.PNG)
            res=driver.find_element(By.XPATH,'/html/body/div[5]/div/h2').text
            assert "123456" in res
            driver.close()
    #
    # @allure.title("用户修改场景")
    # @allure.story("testcase3")
    # def test_web_user_edit(self):
    #     with allure.step("创建浏览器,打开网址"):
    #         driver=webdriver.Chrome()
    #         driver.get("http://10.1.2.14:8080/#/login")
    #         driver.implicitly_wait(10)
    #     with allure.step("清空并输入账号"):
    #         driver.find_element(By.XPATH,'//*[@id="username"]').clear()
    #         driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("admin")
    #     with allure.step("清空并输入密码"):
    #         driver.find_element(By.XPATH,'//*[@id="password"]').clear()
    #         driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("123456")
    #     with allure.step("点击登录按钮"):
    #         driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
    #     with allure.step("打开用户管理"):
    #         driver.get("http://10.1.2.14:8080/#/system/user")
    #     with allure.step("点击修改"):
    #         driver.find_element(By.CSS_SELECTOR,'#app > div > div.main-container.hasTagsView > section > div.app-container > div > div.el-col.el-col-24.el-col-xs-15.el-col-sm-18.el-col-md-20.el-col-lg-20.el-col-xl-20 > div.el-table.el-table--fit.el-table--scrollable-x.el-table--enable-row-transition.el-table--small > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_10.is-center.el-table__cell > div > div > button').click()
    #     with allure.step("输入用户名"):
    #         driver.find_element(By.XPATH,'//form/div[1]/div/div/input').clear()
    #         driver.find_element(By.XPATH,'//form/div[1]/div/div/input').send_keys("111111")
    #     with allure.step("输入手机号"):
    #         driver.find_element(By.XPATH,'//form/div[2]/div/div/input').clear()
    #         driver.find_element(By.XPATH,'//form/div[2]/div/div/input').send_keys("18086473436")
    #     with allure.step("输入昵称"):
    #         driver.find_element(By.XPATH,'//form/div[3]/div/div/input').clear()
    #         driver.find_element(By.XPATH,'//form/div[3]/div/div/input').send_keys("1111")
    #     with allure.step("输入邮箱"):
    #         driver.find_element(By.XPATH,'//form/div[4]/div/div/input').clear()
    #         driver.find_element(By.XPATH,'//form/div[4]/div/div/input').send_keys("111114@163.com")
    #     with allure.step("选择部门"):
    #         driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[2]').click()
    #         driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys("研发部")
    #         driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ARROW_DOWN)
    #         driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ARROW_DOWN)
    #         driver.find_element(By.XPATH,'//form/div[5]/div/div/div[1]/div[1]/div[2]/input').send_keys(Keys.ENTER)
    #     with (allure.step("选择岗位")):
    #         driver.find_element(By.XPATH,'//form/div[6]/div/div/div/input').click()
    #         driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
    #     with allure.step("选择角色"):
    #         driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div > div > div.el-select__tags').click()
    #         sleep(0.5)
    #         driver.find_element(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
    #     with allure.step("点击确认"):
    #         driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[2]/span').click()
    #     with allure.step("断言结果"):
    #         allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),allure.attachment_type.PNG)
    #         res=driver.find_element(By.XPATH,'/html/body/div[5]/div/h2').text
    #         assert "编辑成功" in res
    #         driver.close()
    # @allure.title("用户搜索场景")
    # @allure.story("testcase4")
    # def test_web_user_search(self):
    #     with allure.step("创建浏览器,打开网址"):
    #         driver=webdriver.Chrome()
    #         driver.get("http://10.1.2.14:8080/#/login")
    #         driver.implicitly_wait(10)
    #     with allure.step("清空并输入账号"):
    #         driver.find_element(By.XPATH,'//*[@id="username"]').clear()
    #         driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("admin")
    #     with allure.step("清空并输入密码"):
    #         driver.find_element(By.XPATH,'//*[@id="password"]').clear()
    #         driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("123456")
    #     with allure.step("点击登录按钮"):
    #         driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
    #     with allure.step("打开用户管理"):
    #         driver.get("http://10.1.2.14:8080/#/system/user")
    #     with allure.step("输入搜索条件"):
    #         driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[2]/div[1]/div[1]/div[1]/input').send_keys("111")
    #     with allure.step("输入开始日期"):
    #         driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[2]/div[1]/div[1]/div[2]/input[1]').click()
    #         sleep(0.5)
    #         driver.find_element(By.CSS_SELECTOR,'body > div.el-picker-panel.el-date-range-picker.el-popper > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content.el-date-range-picker__content.is-left > table > tbody > tr:nth-child(3) > td.available.today > div > span').click()
    #         driver.find_element(By.CSS_SELECTOR,'body > div.el-picker-panel.el-date-range-picker.el-popper > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content.el-date-range-picker__content.is-left > table > tbody > tr:nth-child(3) > td.available.today > div > span').click()
    #     with allure.step("选择状态"):
    #         driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[2]/div[1]/div[1]/div[3]/div/input').click()
    #         driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
    #     with allure.step("点击搜索"):
    #         driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div/div[2]/div[1]/div[1]/span/button[1]').click()
    #
    #     with allure.step("断言结果"):
    #         allure.attach(driver.get_screenshot_as_png(),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),allure.attachment_type.PNG)
    #         res=driver.find_element(By.XPATH,'//tbody/tr[1]/td[5]/div').text
    #         assert "18086473436" in res
    #         driver.close()
