#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : myPageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class MyPageLocator:
    """
        我的页面元素
    """
    # 我的 页面
    MyPage_loc = ('id', 'com.chazuo.college.enterprise:id/my')

    # 服务协议勾选框
    agreement_t_loc = ('id', 'com.chazuo.college.enterprise:id/check_box_agree')

    # 手机号登录
    phone_login_loc = ('id', 'com.chazuo.college.enterprise:id/ll_loginbyphone')

    # 切换密码登录
    pwd_login_loc = ('id', 'com.chazuo.college.enterprise:id/actionbar_right_btn')


