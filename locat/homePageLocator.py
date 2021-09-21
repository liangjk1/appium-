#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 16:42
# @Author : ZY
# @File : homePageLocator.py
# @Project : APP
from appium.webdriver.common.mobileby import By


class HomePageLocator:
    """
        首页元素
    """
    # 隐私协议 同意or不同意
    agreement_yes_loc = ('id', 'com.chazuo.college.enterprise:id/tv_confirm')
    agreement_no_loc = ('id', 'com.chazuo.college.enterprise:id/tv_cancel')
    # 推荐页面 跳过
    recommend_loc = ('id', 'com.chazuo.college.enterprise:id/tv_skip')

    # 登录成功关闭福利送
    notice_close_loc = ('id', 'com.chazuo.college.enterprise:id/notice_close')
    # 登录成功后的欢迎页面
    login_success_loc = ('id', 'com.chazuo.college.enterprise:id/tv_name')
    # 首页按钮
    homepage_loc = ('id', 'com.chazuo.college.enterprise:id/day')
    # 优秀学员案例
    testcase_loc = ('xpath', "//*[@text='跟何川老师学习后，我在职场收获了什么？']")
    # 学习内容文字跳转
    learn_page = ('xpath', "//*[@text='于国皓：晋升副总并涨薪150%，我用了这3招']")
    # 开始学习播放按钮
    begin_learn_loc = ('xpath', "//*[@text='播放']")

    # 首页查询
    home_select_loc = ('id', 'com.chazuo.college.enterprise:id/search_layout_main')
    # 查询输入框
    select_loc = ('id', 'com.chazuo.college.enterprise:id/et_search')

    # 查询页面-查询按钮
    selectpage_sel_loc = ('id', 'com.chazuo.college.enterprise:id/search_button')

    # 课程筛选
    select_case_loc = ('xpath', "//*[@text='课程']")

    # 已订阅课程学习
    frist_case_loc = ('xpath', "//*[@text='已订阅']")

    # 文章学习
    page_learn_loc = ('xpath', "//*[@text='6个问题，轻松搞定问题员工']")

    # 返回
    pagereturn_loc = ('xpath', '//android.webkit.WebView/android.view.View[0]/android.view.View[0]/android.view.View[1]')
