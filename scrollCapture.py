from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.google.com/search?q=cat&sxsrf=ALeKk02Qq0CEZiPCljjBdnQ3LdpgDZhWSw:1608973684739&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjOzbmHpuvtAhWXHXAKHe9FAZIQ_AUoAXoECAUQAw&biw=1049&bih=797')

driver.get_screenshot_as_file("data/test0.png")
driver.execute_script("window.scrollTo(0,1000)")

for i in range(1,5):
    scroll_index = i * 1000
    # 0, 1000, 2000, 3000, 4000
    driver.get_screenshot_as_file("data/test" + str(scroll_index) + ".png")

    time.sleep(3)

    driver.execute_script("window.scrollTo(0," + str(scroll_index) + ")")

driver.close()
