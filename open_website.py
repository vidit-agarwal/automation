import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "vidit.agarwala@gmail.com"
pwd=" happy"

driver = webdriver.Firefox(executable_path=r"/home/vidit/software/geckodriver") #path for your webdriver. mine is of firefox
while(1) :
    url = 'https://c.mp.ucweb.com/detail/2cf63e44e5f54390992a5131d0bd2d25' # url which you want to reload again and again
    driver.get(url)
    #assert "Facebook" in driver.title
    driver.implicitly_wait(500)
    time.sleep(5)
