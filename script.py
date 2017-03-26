###############################################
# This code is for putting pritein value and genrating a id for that

###############################################



import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#replace the driver location with ur system driver location of browser. Mine is firefox on Linux .

driver = webdriver.Firefox(executable_path=r"/home/vidit/geckodriver")

url = 'https://www.ebi.ac.uk/interpro/'
driver.get(url)
textbox = driver.find_element_by_id("sequenceBoxId")
textbox.send_keys(">protein\nMAKSSFKISNPLEARMSESSRIREKYPDRIPVIVEKAGQSDVPDIDKKKYLVPADLTVGQFVYVVRKRIKLGAEKAIFVFVKNTLPPTAALMSAIYEEHKDEDGFLYMTYSGENTFGSLTVA") # this is the demo protein value.. we can pass the enitre range of protein value
time.sleep(1)
driver.find_element_by_xpath("//button[@name='submit' and @type='submit']").click() # old page click

driver.implicitly_wait(9)
#driver.get(url_process
#driver.navigate().forward()
text_id = driver.find_element_by_xpath("//div[@class='error_msg']/p[3]/a")
id=text_id.get_attribute("href")
print(id)   # this is the id we want too find
driver.quit()
