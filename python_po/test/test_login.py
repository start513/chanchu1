from selenium import webdriver
import allure
from page.login_page import LoginPage


@allure.feature("登录模块")
class TestUserLogin:
    @allure.story("testcase01")
    @allure.title("管理员成功登录场景")
    def test_gly_login_success(self):
        with allure.step("打开浏览器"):
            driver=webdriver.Chrome()
            login_page=LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("admin")
        with allure.step("输入密码"):
            login_page.set_paw("123456")
        with allure.step("点击登录"):
            login_page.click_login()
        with allure.step("断言结果"):
            assert "系统运行正常" in login_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(),"页面截图",allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/01.png")
        driver.quit()

    @allure.story("testcase02")
    @allure.title("用户1成功登录场景")
    def test_yh1_login_success(self):
        with allure.step("打开浏览器"):
            driver = webdriver.Chrome()
            login_page = LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("user1")
        with allure.step("输入密码"):
            login_page.set_paw("123456")
        with allure.step("点击登录"):
            login_page.click_login()
        with allure.step("断言结果"):
            assert "系统运行正常" in login_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(), "页面截图", allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/02.png")
        driver.quit()


    @allure.story("testcase03")
    @allure.title("用户2成功登录场景")
    def test_yh2_login_success(self):
        with allure.step("打开浏览器"):
            driver=webdriver.Chrome()
            login_page=LoginPage(driver)
        with allure.step("输入账号"):
            login_page.set_name("user2")
        with allure.step("输入密码"):
            login_page.set_paw("abcdef")
        with allure.step("点击登录"):
            login_page.click_login()
        with allure.step("断言结果"):
            assert "系统运行正常" in login_page.text_dy()
        allure.attach(driver.get_screenshot_as_png(),"页面截图",allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/03.png")
        driver.quit()