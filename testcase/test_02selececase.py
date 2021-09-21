import time

import pytest

from common.basePage import BasePage
from testcase.conftest import driver
from log_ri_zhi.logHandler import LogHandler
from locat.homePageLocator import HomePageLocator as loc_m

driver = driver


@pytest.mark.usefixtures('homepage')
class Testselectcase:
    logger = LogHandler.logger

    @pytest.mark.parametrize('msg', [["有效管理问题员工"]])
    def test_selectcase(self, msg):
        BasePage(driver).click_element(loc_m.homepage_loc, "点击首页跳转")
        time.sleep(2)
        BasePage(driver).click_element(loc_m.home_select_loc, "点击首页查询跳转")
        BasePage(driver).click_element(loc_m.select_loc, "点击查询框")
        BasePage(driver).input_element(msg, loc_m.select_loc, "输入查询内容")
        BasePage(driver).click_element(loc_m.selectpage_sel_loc, "点击查询")
        time.sleep(1)
        BasePage(driver).click_element(loc_m.select_case_loc, "切换课程查询内容")
        BasePage(driver).click_element(loc_m.frist_case_loc, "选择已订阅课程")
        BasePage(driver).click_element(loc_m.page_learn_loc, "进入文章阅读")
        time.sleep(0.5)
        BasePage(driver).swipeUp(n=1)
        time.sleep(2)
        BasePage(driver).ipswRight(n=3)
        time.sleep(2)


if __name__ == '__main__':
    pytest.main(['-s', 'test_02selececase.py'])
