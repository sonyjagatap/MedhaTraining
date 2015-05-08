#valid username and valid passwd
import selenium
from selenium import webdriver
from libYSeln import *

browser = webdriver.Firefox()
browser.get("https://www.yahoo.com")
browser.implicitly_wait(10)

mailele = findByXpath(browser,"//div/div/a/em")
mailele.click()
#/html/body/div[1]/div[2]/div[2]/div/div/ul/li[3]/div/div/a/em

username = findById(browser,"login-username")
username.send_keys("sony.jagatap")

password = findById(browser,"login-passwd")
password.send_keys("khushi0412")

loginbutton = findById(browser,"login-signin")
loginbutton.click()
browser.implicitly_wait(10)

print browser.title

try:
	assert("Yahoo" == browser.title)
except:
	print "ERROR: Testcase Failed"
else:
	print "Test case Passed"