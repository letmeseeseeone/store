'''
    任务4：
        知乎搜索一篇文章。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉选项
from selenium.webdriver.common.action_chains import ActionChains  #复选框
import time

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/explore")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="guestSquare"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/a').click()
driver.find_element(By.XPATH,'//html/body/div[4]/div/div/div/div[2]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/div/div/div/button').click()
time.sleep(3)

driver.quit()

