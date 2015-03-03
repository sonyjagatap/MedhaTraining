#valid username and valid passwd
import selenium
from selenium import webdriver
from libSeln import *

driver = webdriver.Firefox()
driver.get("http://facebook.com")

username = findById(driver,"email")
username.send_keys("jwoo1459@gmail.com")

password = findById(driver,"pass")
password.send_keys("John2015")

driver.implicitly_wait(1)
loginbutton = findById(driver,"loginbutton")
loginbutton.click()



try:
	assert("Facebook" == driver.title)
except:
	print "Error: Test Case FAILED"
else:
	print "Info: Test Case PASSED"

