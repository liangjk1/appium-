import time

import pytest

from common.basePage import BasePage
from testcase.conftest import driver
from log_ri_zhi.logHandler import LogHandler
from locat.homePageLocator import HomePageLocator as loc_m

driver = driver


@pytest.mark.usefixtures('homepage')
class TestLearnCase:
    logger = LogHandler.logger

    def test_learn(self):
        # BasePage(driver).click_element(loc_m.notice_close_loc, '关闭福利推荐')
        BasePage(driver).click_element(loc_m.homepage_loc, "点击首页跳转")
        time.sleep(2)
        BasePage(driver).swipeUp(n=2)
        BasePage(driver).click_element(loc_m.testcase_loc, "点击优秀学员按案例")
        BasePage(driver).click_element(loc_m.learn_page, "学习内容页面跳转")
        time.sleep(1)
        BasePage(driver).click_element(loc_m.begin_learn_loc, "播放音频")
        time.sleep(2)
        BasePage(driver).swipeUp()
        time.sleep(2)
        BasePage(driver).close_app()


if __name__ == '__main__':
    pytest.main(['-s', 'test_03learncase.py'])
