#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:37
# @Author : ZY
# @File : loginPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class LoginPageLocator:
    """
        登录页元素
    """
    # 手机号
    username_loc = ('id', 'com.chazuo.college.enterprise:id/cet_phonenum')
    # 密码
    pwd_loc = ('id', 'com.chazuo.college.enterprise:id/cet_password')
    # 登录
    login_button_loc = ('id', 'com.chazuo.college.enterprise:id/tv_login')
