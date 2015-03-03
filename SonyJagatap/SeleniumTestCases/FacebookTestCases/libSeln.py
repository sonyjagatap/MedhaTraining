import selenium
from selenium import webdriver

def findById(driver,id):
	we=""
	try:
		we = driver.find_element_by_id(id)
	except:
		print "ERROR: ById element NOT found"
	else:
		return we

def findByLinkText(driver,linktext):
	we=""
	try:
		we = driver.find_element_by_link_text(linktext)
	except:
		print "ERROR: By LinkTest element NOT found"
	else:
		return we

def findByXpath(driver,xpath):
	we=""
	try:
		we = driver.find_element_by_xpath(xpath)
	except:
		print "ERROR: By LinkTest element NOT found"
	else:
		return we