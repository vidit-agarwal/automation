import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = "vidit.agarwala@gmail.com"
pwd=" happy"

driver = webdriver.Firefox(executable_path=r"/home/vidit/software/geckodriver")
while(1) :
    url = 'https://c.mp.ucweb.com/detail/0e2f64b80e3d46fc90c10d5b6b5e7956'
    driver.get(url)
    #assert "Facebook" in driver.title
    #driver.implicitly_wait(500)
    time.sleep(5)
