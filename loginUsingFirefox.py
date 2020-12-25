from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip


# FireFox 드라이버의 경로를 설정합니다.
driver = webdriver.Firefox(executable_path='./geckodriver')

# 접속할 url
url = "https://nid.naver.com/nidlogin.login"

# 접속 시도
driver.get(url)

login = {
    "id" : "61459",
    "pw" : "password"
}


def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)


clipboard_input('//*[@id="id"]', login.get("id"))
clipboard_input('//*[@id="pw"]', login.get("pw"))
driver.find_element_by_xpath('//*[@id="log.login"]').click()


# driver.get("https://pann.nate.com/")
#
# driver.find_element_by_class_name("more_date").click()
# driver.close()
