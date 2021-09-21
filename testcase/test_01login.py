# 把driver传过来
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from locat.loginPageLocator import LoginPageLocator as loc_l
from locat.homePageLocator import HomePageLocator as loc_m
from locat.myPageLocator import MyPageLocator as loc_a
from common.basePage import BasePage
from log_ri_zhi.logHandler import LogHandler
from testcase.conftest import driver

# 把driver传过来
driver = driver


@pytest.mark.usefixtures('login')
class TestLogin:
    logger = LogHandler.logger

    # 账号错误
    @pytest.mark.parametrize('user,password', [["15521507901", "test123"]])
    def testlogin_False1(self, user, password):
        BasePage(driver).input_element(user, loc_l.username_loc, "登录页-输入账号")
        BasePage(driver).input_element(password, loc_l.pwd_loc, "登录页-输入密码")
        BasePage(driver).click_element(loc_l.login_button_loc, "登录页-点击登录")
        time.sleep(2)
        assert BasePage(driver).get_toast('用户不存在', '登录页面下-输入错误的账号') == '用户不存在'

    # 密码错误
    @pytest.mark.parametrize('user,password', [["15521507903", "test12345"]])
    def testlogin_False2(self, user, password):
        BasePage(driver).input_element(user, loc_l.username_loc, "登录页-输入账号")
        BasePage(driver).input_element(password, loc_l.pwd_loc, "登录页-输入密码")
        BasePage(driver).click_element(loc_l.login_button_loc, "登录页-点击登录")
        time.sleep(2)
        assert BasePage(driver).get_toast('密码错误', '登录页面下-输入错误的密码') == '密码错误'
        # # 用于生成xpath定位 相当于 "//*[@text='密码错误']"
        # toast_message = "密码错误"
        # message = '//*[@text=\'{}\']'.format(toast_message)
        # # 获取toast提示框内容
        # toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
        # print(toast_element.text)
        # assert toast_element.text == "密码错误"

        # 正常登录,正确的账号，正确的密码

    @pytest.mark.parametrize('user,password', [["15521507903", "test123"]])
    def test_login_sucess(self, user, password):
        BasePage(driver).input_element(user, loc_l.username_loc, "登录页-输入账号")
        BasePage(driver).input_element(password, loc_l.pwd_loc, "登录页-输入密码")
        BasePage(driver).click_element(loc_l.login_button_loc, "登录页-点击登录")
        time.sleep(2)
        # 5，断言获取用户名和预期结果是否相同
        if BasePage(driver).get_element_text(loc_a. phone_login_loc, "判断是否成功登录") == "手机号登录":
            # 3. 同意服务协议
            BasePage(driver).click_element(loc_a.agreement_t_loc, "首页-服务协议勾选框")
            print('2')
            # 4. 手机号登录
            BasePage(driver).click_element(loc_a.phone_login_loc, "首页-手机号登录")
            print('3')
            # 5. 切换密码登录
            BasePage(driver).click_element(loc_a.pwd_login_loc, "首页-切换密码登录")
            BasePage(driver).input_element(user, loc_l.username_loc, "登录页-输入账号")
            BasePage(driver).input_element(password, loc_l.pwd_loc, "登录页-输入密码")
            BasePage(driver).click_element(loc_l.login_button_loc, "登录页-点击登录")
            time.sleep(2)
            assert BasePage(driver).get_element_text(loc_m.login_success_loc, "我的页面-获取登录用户名") == "Hi，用户7903"
        else:
            assert BasePage(driver).get_element_text(loc_m.login_success_loc, "我的页面-获取登录用户名") == "Hi，用户7903"
