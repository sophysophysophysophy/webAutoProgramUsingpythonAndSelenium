from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("./chromedriver")
driver.get("https://gallery.v.daum.net/p/viewer/5015999")

time.sleep(2)
action = ActionChains(driver)

action.move_to_element(driver.find_element_by_xpath('//*[@id="mArticle"]/div[3]/div/div[1]/a[1]/div/img')).perform()

