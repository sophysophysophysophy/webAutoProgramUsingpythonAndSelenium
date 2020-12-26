from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# https://read-write-developer.tistory.com/118
driver.get('https://read-write-developer.tistory.com')


# id, name, selector, xPath

# # selector로 element 찾기
# driver.find_element_by_css_selector('#content > div.inner > div:nth-child(1)').click()
#
# # name, password, comment
# driver.find_element_by_name("comment").send_keys("댓글 입력 예제입니다.")
# driver.find_element_by_name("name").send_keys("이름 부분입니다.")
# driver.find_element_by_name("password").send_keys("123123")
# # driver.find_element_by_xpath('//*[@id="secret"]').click()
# driver.find_element_by_xpath('//*[@id="entry118Comment"]/div/form/div/div[1]/div/label').click()
# driver.find_element_by_class_name("btn").click()
#
#
#
# # refresh
# driver.refresh()
#
#
#
# driver.find_element_by_css_selector('#content > div.inner > div:nth-child(1)').click()
#
# # name, password, comment
# driver.find_element_by_name("comment").send_keys("댓글 입력 예제입니다.")
# driver.find_element_by_name("name").send_keys("이름 부분입니다.")
# driver.find_element_by_name("password").send_keys("123123")
# # driver.find_element_by_xpath('//*[@id="secret"]').click()
# driver.find_element_by_xpath('//*[@id="entry118Comment"]/div/form/div/div[1]/div/label').click()
# driver.find_element_by_class_name("btn").click()

# 반복문 만들기
count = 0
while count < 5:
    driver.find_element_by_css_selector('#content > div.inner > div:nth-child(1)').click()

    # name, password, comment
    driver.find_element_by_name("comment").send_keys("댓글 입력 예제입니다.")
    driver.find_element_by_name("name").send_keys("이름 부분입니다.")
    driver.find_element_by_name("password").send_keys("123123")
    # driver.find_element_by_xpath('//*[@id="secret"]').click()
    driver.find_element_by_xpath('//*[@id="entry118Comment"]/div/form/div/div[1]/div/label').click()
    driver.find_element_by_class_name("btn").click()
    driver.refresh()
    count = count + 1


driver.close()
