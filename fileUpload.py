from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("http://the-internet.herokuapp.com/upload")

driver.find_element_by_id("file-upload").send_keys("/Users/jeonghyeonju/IdeaProjects/PycharmProjects/webAutoProgramUsingpythonAndSelenium/data/test.png")
