from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

#Init Chrome & Driver
#service = Service(executable_path=r'E:\chrome\chrome-win64\chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
#wd = webdriver.Chrome(service=service, options=chrome_options)
wd = webdriver.Chrome(options=chrome_options)
wd.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 
          'params':{'behavior':'allow', 'downloadPath':r"D:\temp"}}
wd.execute("send_command", params=params)
ids = ["232819975", "227381705", "234538655"]

def loginwjx():
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get('https://www.wjx.cn/login.aspx')

    # 登陆操作
    wd.find_element(By.ID, 'UserName').send_keys('18125835030')
    wd.find_element(By.ID, 'Password').send_keys('zzy782003600')
    wd.find_element(By.ID, 'LoginButton').click()
    time.sleep(3)

def download_excel_start(ids):
    for id in ids:
        url = "https://www.wjx.cn/wjx/activitystat/viewstatsummary.aspx?activity=" + id + "&reportid=0&dw=1&dt=0"
        print(url)
        wd.get(url)
        time.sleep(5)
              
loginwjx()
download_excel_start(ids)
#默认下载地址Downloads
print('wait for 20 seconds....')
time.sleep(20)
