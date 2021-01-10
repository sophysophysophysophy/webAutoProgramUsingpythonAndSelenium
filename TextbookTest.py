from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
#
# # driver.get('https://class101.net')
# driver.get('https://class101.net/login?redirect=%2F')
#

driver.get('https://class101.net/classes/5eb662b1a009382541b516db/contents/5f8eb1ab00b93b0021dea1b6')

login = {
    "id" : "61459@naver.com",
    "pw" : "test"
}

driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/main/div/div[1]/div/div/p/button').send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys(login.get("id"))

driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys(login.get("pw"))
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
#
#
# driver.get('https://class101.net/me/classes')



# driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/main/div/div/div[1]/div[5]').screenshot('data/' + str(i) + '.png')


time.sleep(10)
driver.get_screenshot_as_file('data/testclass101.png')
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/main/div/div/div[1]/div[5]').screenshot('data/testclass101.png')
dta = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/main/div/div/div[1]/div[5]/div[2]/div')
dta.screenshot('data/testclass.png')
# driver.close()
