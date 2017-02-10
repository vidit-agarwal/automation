import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "vidit.agarwala@gmail.com"
pwd=" happy"

driver = webdriver.Firefox(executable_path=r"/home/vidit/software/geckodriver")
while(1) :
    url = 'http://c.mp.ucweb.com/detail/a068d381d4594cd388161d9a05983c31'
    driver.get(url)
    #assert "Facebook" in driver.title
    #driver.implicitly_wait(500)
    time.sleep(5)
