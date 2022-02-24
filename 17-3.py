# 任务3:
# 去b站，搜索一个视频，点赞


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉选项
from selenium.webdriver.common.action_chains import ActionChains  #复选框
import time

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="i_cecream"]/main/section[1]/div[1]/div[5]/div[2]/a/div/div[1]/picture/img').click()
driver.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()
driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div[3]/div[2]/div[1]/input').send_keys("账号")
driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div[3]/div[2]/div[1]/input').send_keys("密码")
driver.find_element(By.XPATH,'//html/body/div[6]/div/div[2]/div[3]/div[3]/div[2]').click()
driver.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()


driver.quit()