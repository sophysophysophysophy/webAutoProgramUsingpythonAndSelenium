from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://read-write-developer.tistory.com')
driver.get_screenshot_as_file('data/test.png')
driver.close()
