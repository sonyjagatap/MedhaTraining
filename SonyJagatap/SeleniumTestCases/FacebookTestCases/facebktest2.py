#invalid username and valid passwd
import selenium
from selenium import webdriver
from libSeln import *

driver = webdriver.Firefox()
driver.get("http://facebook.com")

username = findById(driver,"email")
username.send_keys("test007")

password = findById(driver,"pass")
password.send_keys("John2015")

driver.implicitly_wait(1)
loginbutton = findById(driver,"loginbutton")
loginbutton.click()

driver.implicitly_wait(10)
errorele = findByXpath(driver,"//div/form/div[2]/div[1]")
errorText = errorele.text
print errorText
#/html/body/div/div[2]/div[1]/div/div/div[2]/div/form/div[2]/div[1]

try:
	assert(errorText == "Please re-enter your password")
except:
	print "Error: Test Case FAILED"
else:
	print "Info: Test Case PASSED"

