from selenium import webdriver
from selenium.webdriver.common.keys import Keys # you will need to download selenium from pip / from their website and the drivers
from time import sleep

class insta_bot():

	def __init__(self,usrname,pswrd):
		#going to the website
		browser.get("http://instagram.com")
		sleep(2)
		#finding the username and password input area and filling them
		logindets = browser.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(usrname)
		logindets = browser.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pswrd)
		#the button to login is "submit" type , so using that to find it and clicking it
		logindets = browser.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(5)
		#this is used to click on Not now button in the notifications , can be removed if its not shown
		browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
		sleep(3)

	def quit(self,secs):
		sleep(secs)
		#command to close the browser 
		browser.quit()

	def finduser(self,name):
		#finding the search bar and entering name 
		browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
			.send_keys(name + Keys.RETURN)
		sleep(2)
		#to click on the searched name
		browser.find_element_by_xpath("//a[contains(@href,'/{}')]".format(name))\
			.send_keys(Keys.RETURN)
		sleep(5)

def first_post(): 
	# finds the first post 
	pic = browser.find_element_by_class_name("_9AhH0") 
	pic.click() # clicks on the first post 

def like_post(): 
	sleep(2) 
	like = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button') 
	# finding the like button
	sleep(2) 
	like.click() # clicking the like button

def next_post(): 
	sleep(2) 
	# finds the button which gives the next post 
	nex = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
	sleep(1) 
	return nex 

def like_till_the_end(): 
	next_el = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
	while(True): 
		# if next button is there then 
		if next_el != False: 
			# click the next button 
			next_el.click() 
			sleep(2) 
			# like the post 
			like_post()	 
			sleep(2)			 
		else: 
			print("The End")  #it will show an error at the end , recommended to fix it 
			break
		next_el = next_post()


username = input("Enter the username of your account : ")
password = input("Enter the password of your account : ")
like_acc = input("Enter the Account name you want to spam likes : ")
exe_path = input("Enter the path of your driver : ")
global browser
browser = webdriver.Firefox(executable_path = exe_path)

my_bot = insta_bot(username,password)
my_bot.finduser(like_acc)

first_post() 
like_post() 
like_till_the_end()


my_bot.quit(5)

