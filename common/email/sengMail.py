#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 11:44
# @Author : ZY
# @File : sengMail.py
# @Project : APP
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yagmail

from dataDriver.yamlData import readYaml


def send_mail():
    # logger = LogHandler.logger
    # s = readYaml("seng.yml")
    # try:
    #     yag = yagmail.SMTP(user=s['sendEmailUser'], host="smtp.qq.com", password=s['sendPassword'])
    #     contents = []
    #     contents.extend(s['contents'])
    #
    #     # contents.append(s['fileName'])
    #     contents.append(yagmail.inline(s["attachment"]))
    #     yag.send(s['acceptEmailUser'], s['title'], contents)

    #
    #     yagmail.SMTP.close(yag)
    #     print('自动化测试报告邮件成功发送！')
    # except Exception as e:
    #     print('邮件报告发送失败！')
    #     raise

    """
        发送测试报告到邮箱
        :param report_name: 需要发送的测试报告
        :param receiver: 邮件接收人
        :return:
    """
    # ----------------------------------------------------------
    s = readYaml("E:/pythonProject1/common/email/seng.yml")
    contents = []
    contents.extend(s['contents'])
    # 获取邮件正文,读取测试报告的内容
    # f = open('E:/pythonProject1/output/report/index.html', 'rb')
    # mail_body = f.read()
    #
    mail_body = contents
    # 邮件服务器
    smtpserver = 'smtp.qq.com'
    # 发件人和密码
    sender = '364390447@qq.com'
    password = 'trqbcoxdmusabjcf'
    # 接收人
    receiver = '364390447@qq.com'
    # 邮件主题
    subject = u'自动化测试报告'
    # ----------------------------------------------------------
    # 连接登录邮箱
    server = smtplib.SMTP(smtpserver, 25)
    server.login(sender, password)
    # ----------------------------------------------------------
    # 添加附件
    sendfile = open('E:/pythonProject1/output/report/index.html', 'rb').read()
    att = MIMEText(str(sendfile), "base64", 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    msg = MIMEMultipart('related')
    msgtext = MIMEText(str(mail_body), 'html', 'utf-8')
    msg.attach(msgtext)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg.attach(att)
    # ----------------------------------------------------------
    # 发送邮件
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
    # logger.info("发送成功!")
    print("报告邮件发送成功!")


if __name__ == '__main__':
    send_mail()
