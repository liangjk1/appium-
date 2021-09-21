import os

import pytest

from common.email.sengMail import send_mail

if __name__ == '__main__':

    pytest.main()

    # 生成allure报告
    os.system('allure generate ../output/temp -o ../output/report --clean')
    send_mail()