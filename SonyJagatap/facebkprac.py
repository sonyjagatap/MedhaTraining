#login in facebook and post amessage
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://www.facebook.com")

EmailElement = browser.find_element_by_id("email")
EmailElement.clear()
EmailElement.send_keys("jwoo1459@gmail.com")

PassWordElement = browser.find_element_by_id("pass")
PassWordElement.clear()
PassWordElement.send_keys("John2015")

LoginButton = browser.find_element_by_id("loginbutton").click()
browser.implicitly_wait(10)

try:
	assert(browser.title == "Facebook")
except:
	print "Error: Login failed"
else:
	print "Login succesful"


# Post a message
TextElementBox = browser.find_element_by_xpath("//div[2]/div/div/textarea")
TextElementBox.send_keys("Hi everyone")
PostButton = browser.find_element_by_xpath("//div/ul/li[2]/button").click()
# /html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/form/div/div[5]/div/ul/li[2]/button

# Find a friend
# /html/body/div[1]/div[1]/div/div/div[1]/div/div/div[2]/form/div/div/div/div/div[3]
#TextElementBox = browser.find_element_by_id("u_0	_d")
#TextElementBox.send_keys("training")
