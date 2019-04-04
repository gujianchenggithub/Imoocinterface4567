import  smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    smtpserver='smtp.163.com'
    user='gujiancheng1989@163.com'
    password='gu15925686072'

    sender='gujiancheng1989@163.com'
    receives=['1046662346@qq.com','2819992623@qq.com']

    subject='Web Selenium 自动化测试报告'
    content='<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']='gujiancheng1989@163.com'
    msg['To']=','.join(receives)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    print("Start send Email...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send Email end!")
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

