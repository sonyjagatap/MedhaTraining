#no username and no paswd
import selenium
from selenium import webdriver
from libSeln import *

driver = webdriver.Firefox()
driver.get("http://facebook.com")

username = findById(driver,"email")
username.send_keys("")

password = findById(driver,"pass")
password.send_keys("")

driver.implicitly_wait(1)
loginbutton = findById(driver,"loginbutton")
loginbutton.click()

driver.implicitly_wait(10)
errorele = findByXpath(driver,"//div/form/div[2]/div[1]")
errorText = errorele.text
print errorText

try:
	assert(errorText == "Incorrect Email")
except:
	print "Error: Test Case FAILED"
else:
	print "Info: Test Case PASSED"
