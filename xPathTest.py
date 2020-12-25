from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("인생이란 무엇인가")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

# xPath로 정확한 element 찾기
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[4]/a').click()

