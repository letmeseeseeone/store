# 任务1：
# 京东、淘宝登陆，搜索一个商品，点击详情。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉选项
from selenium.webdriver.common.action_chains import ActionChains  #复选框
import time

driver = webdriver.Chrome()            # 创建谷歌浏览器对象
driver.get("http://www.taobao.com")
driver.maximize_window()       # 窗口最大化
driver.find_element(By.XPATH,'//*[@id="q"]').send_keys("苹果13")     #寻找搜索输入框
driver.find_element(By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button').click()    # 点击一下按钮
driver.find_element(By.XPATH,'//*[@id="fm-login-id"]').send_keys("*****")
driver.find_element(By.XPATH,'//*[@id="fm-login-password"]').send_keys("****")

#获取滑块
ele = driver.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ac = ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(300,0).perform()
ac.release()  # 释放鼠标

# time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="login-form"]/div[4]/button').click()
driver.find_element(By.XPATH,'//*[@id="mx_5"]/ul/li[1]/a/img').click()
#
#
time.sleep(3)
# 退出浏览器
driver.quit()