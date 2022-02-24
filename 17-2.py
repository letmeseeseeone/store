'''
    任务2：
        苏宁，国美，搜索一个商品，添加购物车。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉选项
from selenium.webdriver.common.action_chains import ActionChains  #复选框
import time

driver=webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="searchKeywords"]').send_keys("苹果13")
driver.find_element(By.XPATH,'//*[@id="searchSubmit"]').click()
driver.find_element(By.XPATH,'//*[@id="ssdsn_search_pro_fn-synonym_1_01:0000000000_12313015493"]').click()
driver.find_element(By.XPATH,'//*[@id="addCart"]').click()

driver.quit()