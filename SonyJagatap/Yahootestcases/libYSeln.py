#creating library
import selenium
from selenium import webdriver

def findById(browser,id):
	we=""
	try:
		we = browser.find_element_by_id(id)
	except:
		print "ERROR: ById element not found"
	else:
		return we 

def findByLinktext(browser,linktext):
	we=""
	try:
		we =browser.find_element_by_linktext(linktext)
	except:
		print "ERROR: ByLinktext element not found"
	else:
		return we

def findByXpath(browser,xpath):
	we=""
	try:
		we = browser.find_element_by_xpath(xpath)
	except:
		print "ERROR ByXpath element not found"
	else:
		return we		