#valid username and invalid passwd
import selenium
from selenium import webdriver
from libYSeln import *

browser = webdriver.Firefox()
browser.get("https://www.yahoo.com")
browser.implicitly_wait(10)

mailele = findByXpath(browser,"//div/div/a/em")
mailele.click()

username = findById(browser,"login-username")
username.send_keys("")

password = findById(browser,"login-passwd")
password.send_keys("")

loginbutton = findById(browser,"login-signin")
loginbutton.click()
browser.implicitly_wait(10)

errorele = findById(browser,"mbr-login-error")
errorText = errorele.text
print errorText

try:
	assert(errorText == "Invalid ID or password.\n"
		"Please try again using your full Yahoo ID.")
except:
	print "ERROR: Test case Failed"
else:
	print "Test case Passed"