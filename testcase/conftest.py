#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 15:42
# @Author : ZY
# @File : conftest.py
# @Project : APP
import time

from appium import webdriver
import pytest
from common.allPathSet import AllPathSet
from common.basePage import BasePage
from locat.homePageLocator import HomePageLocator as loc_h
from locat.loginPageLocator import LoginPageLocator as loc_l
from locat.myPageLocator import MyPageLocator as loc_m

import os

"""
    conftest夹具
"""


def baseDriver():
    # 构造参数
    desired_capabilities = AllPathSet.DEVICE_PATH
    # print(desired_capabilities)
    # 向服务端发送连接信息
    driver = webdriver.Remote(AllPathSet.APPIUM_HTTP_PATH, desired_capabilities)
    driver.implicitly_wait(10)
    return driver
    # driver.close_app()


driver = baseDriver()


@pytest.fixture(scope="module")
def login():
    # 1，进入首页
    # BasePage(driver).click_element(loc_h.agreement_yes_loc, "隐私协议-同意")
    # BasePage(driver).click_element(loc_h.recommend_loc, "推荐页面-跳过")

    # 2，进入我的页面
    BasePage(driver).click_element(loc_m.MyPage_loc, "首页-点击我的")
    print('1')
    # 3. 同意服务协议
    BasePage(driver).click_element(loc_m.agreement_t_loc, "首页-服务协议勾选框")
    print('2')
    # 4. 手机号登录
    BasePage(driver).click_element(loc_m.phone_login_loc, "首页-手机号登录")
    print('3')
    # 5. 切换密码登录
    BasePage(driver).click_element(loc_m.pwd_login_loc, "首页-切换密码登录")

    # yield
    # driver.close_app()


@pytest.fixture(scope="module")
def homepage():
    BasePage(driver).click_element(loc_h.homepage_loc, "进入首页")
    # yield
    # driver.close_app()
