# -*- coding:utf-8 -*-
import time

from selenium import webdriver


driver = webdriver.Chrome(r"D:\pycharm\pythonProject1\script\chromedriver.exe")

driver.get("https://yan.sisurl.com/forum/logging.php?action=login&step=last&formhash=e1905271&cookietime=315360000")
time.sleep(3)
data = driver.find_element("id", "verifyTips").text
print(data)

if data[-2:] == "数字":
    flag = True
else:
    flag = False

data1 = driver.find_elements("class name", "clickVerifyEm")
for i in data1:
    if i.text.isdigit() is flag:
        i.click()

driver.find_element("id", "username").send_keys("rickhhhh")
driver.find_element("id", "nextBtn").click()
time.sleep(3)
driver.find_element("id", "username").send_keys("rickhhhh")
driver.find_element("id", "password").send_keys("wlh171515@")
time.sleep(1)
driver.find_element("id", "loginsubmit").click()
time.sleep(1)
driver.refresh()

input()



