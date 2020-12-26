from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.com/search?q=dog&tbm=isch&hl=ko&tbs=il:cl&sa=X&ved=0CAAQ1vwEahcKEwiYucqXr-vtAhUAAAAAHQAAAAAQAg&biw=716&bih=782")

# driver.find_element_by_xpath()

for i in range(1,4):
    driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) +']/a[1]/div[1]/img').screenshot('data/' + str(i) + '.png')


driver.close()
