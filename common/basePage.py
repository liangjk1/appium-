#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/12 11:35
# @Author : ZY
# @File : basePage.py
# @Project : APP
from time import sleep

from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from log_ri_zhi.logHandler import LogHandler
from common.allPathSet import AllPathSet

"""
    公共类，写公共方法
"""


class BasePage:
    logger = LogHandler.logger

    def __init__(self, driver: Remote):
        self.driver = driver

    def get_element_object(self, loc, info):
        """
        定位元素
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :return: 定位到的元素
        """
        try:
            m = self.driver.find_element(*loc)
            self.logger.info(f"{info}下的{loc}元素找到了")
            return m
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素没找到，原因是{e}")
            raise

    # 显性等待
    def wait(self, loc, info, timeout=25):
        """
        显性等待，失败截图
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
        except:
            self.logger.info(f"{info}下的{loc}元素等待失败")
            # 失败截图
            self.screenshort(info)
            raise

    def click_element(self, loc, info, timeout=25):
        """
        点击，失败截图
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            self.get_element_object(loc, info).click()
            self.logger.info(f"{info}下的{loc}元素点击成功")
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素点击失败")
            # 失败截图
            self.screenshort(info)
            raise

    def input_element(self, msg, loc, info, timeout=25):
        """
        输入内容，失败截图
        :param msg: 输入的内容
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            self.get_element_object(loc, info).send_keys(msg)
            self.logger.info(f"{info}下的{loc}元素输入{msg}成功")
        except Exception as e:
            self.logger.info(f"{info}下的{loc}元素输入{msg}失败")
            # 失败截图
            self.screenshort(info)
            raise

    def get_element_text(self, loc, info, timeout=25):
        """
        获取文本，包括toast
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            self.wait(loc, info, timeout)
            t = self.get_element_object(loc, info).text
            self.logger.info(f"获取{info}下的{loc}元素文本  {t}成功")
            return t
        except Exception as e:
            self.logger.info(f"获取{info}下的{loc}元素文本失败")
            # 失败截图
            self.screenshort(info)
            raise

    def get_element_toast(self, loc, info, timeout=25):
        """
        获取文本，包括toast
        :param loc: 例子：(By.ID, "com.tal.kaoyan:id/tip_commit")
        :param info: 例子：功能模块，描述功能（红包页面）
        :param timeout: 最大显性等待时间，默认25秒
        :return: 无
        """
        try:
            # self.wait(loc, info, timeout)
            t = self.get_element_object(loc, info).text
            self.logger.info(f"获取{info}下的{loc}元素文本{t}点成功")
            return t
        except Exception as e:
            self.logger.info(f"获取{info}下的{loc}元素文本失败")
            # 失败截图
            self.screenshort(info)
            raise

    def screenshort(self, info):
        """
        截图和时间
        :param info: 例子：功能模块，描述功能（红包页面）
        :return: 无
        """
        self.driver.save_screenshot(AllPathSet.SCREENSHORT_Path(info))

    # 根据坐标点击
    def zuobiao(self, xz, yz):
        try:
            WebDriverWait(self.driver, 10).until(self.driver.tap(([(xz, yz)])))
        except:
            pass

    def get_toast(self, news, info):

        try:
            # 用于生成xpath定位 相当于 "//*[@text='用户不存在']"
            toast_message = news
            message = '//*[@text=\'{}\']'.format(toast_message)
            # 获取toast提示框内容
            toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            self.logger.info(f"{info}下的{news}弹窗文本获取成功！")
            return toast_element.text

        # print(toast_element.text)
        # assert toast_element.text == info1
        except Exception as e:
            self.logger.info(f"未获取到弹窗文本信息")
            # 失败截图
            self.screenshort(news)
            raise

    def swipeUp(self, t=500, n=1):
        """向上滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.22

        for i in range(n):
            sleep(1)
            self.driver.swipe(x1, y1, x1, y2, t)
        self.logger.info("向上滑动屏幕")

    def swipeDown(self, t=500, n=1):
        """向下滑动屏幕"""
        l = self.driver.get_window_size()
        print(l['width'])
        print(l['height'])
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        sleep(3)
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
        self.logger.info("向下滑动屏幕")

    def swipLeft(self, t=500, n=1):
        """向左滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
        self.logger.info("向左滑动屏幕")

    def ipswRight(self, t=500, n=1):
        """向右滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.01
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.99

        for i in range(n):
            sleep(1)
            self.driver.swipe(x1, y1, x2, y1, t)
        self.logger.info("向右滑动屏幕")

    def close_app(self):
        self.driver.close_app()
