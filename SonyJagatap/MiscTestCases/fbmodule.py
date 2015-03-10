import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def openWebPage(url):
	browser=webdriver.Firefox()
	browser.get(url)
	return browser

def sendtexttoelement(element, value):
	element.clear()
	element.send_keys(value)
	
def findElementbyId(browser,id):
	try:
		webelement=browser.find_element_by_id(id)
	except:
		print "not able to find the element"
	else:
		return webelement

def login(browser,username, password):
	#EmailElement=browser.find_element_by_id("email")
	EmailElement=findElementbyId(browser,"email")
	#EmailElement.clear()
	#EmailElement.send_keys(username)
	sendtexttoelement(EmailElement,username)
	#PassWordElement=browser.find_element_by_id("pass")
	PassWordElement=findElementbyId(browser,"pass")
	#PassWordElement.clear()
	#PassWordElement.send_keys(password)
	sendtexttoelement(PassWordElement,password)
	#browser.find_element_by_id("loginbutton").click()
	findElementbyId(browser,"loginbutton").click()
	browser.implicitly_wait(10)
	try:
		assert("Facebook"==br.title)
	except:
		print "login failed"
	else:
		print "login successful"
	
# Search a friend
def searchFriend(browser, friendname):
	browser.implicitly_wait(10)
	browser.find_element_by_id("findFriendsNav").click()
	browser.implicitly_wait(10)
	#browser.find_element_by_css_selector("div._586i").send_keys(friendname)
	frboxelement=browser.find_element_by_css_selector("div._586i")
	sendtexttoelement(frboxelement,friendname)
	browser.find_element_by_xpath("//div[2]/button").click()
	browser.implicitly_wait(10)

#Click Status and add text to post
def Postamessage(browser,addtext):
	browser.find_element_by_link_text("Home").click()
	browser.implicitly_wait(10)
	testboxelement=browser.find_element_by_id("u_jsonp_3_d")
	#testboxelement=browser.find_element_by_name('xhpc_message_text')
	sendtexttoelement(testboxelement,addtext)
	#testboxelement.clear()0
	#testboxelement.send_keys("Hi all")
	#browser.find_element_by_id("u_jsonp_2_o").clear()
	#browser.find_element_by_id("u_jsonp_2_o").send_keys("Hi all")
	browser.implicitly_wait(5)
	browser.find_element_by_xpath("//*[contains(text(),'Post')]").click()


	
# MAIN PROGRAM
br = openWebPage("https://wwww.facebook.com")
login(br, "jwoo1459@gmail.com","John2015")
#login("quintanaway1609@gmail.com","Quint1609")
searchFriend(br, "training")
Postamessage(br, "Hello Everyone, Today is Tuesday")