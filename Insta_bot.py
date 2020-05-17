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

def follow():
	sleep(1)
	browser.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()

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
		try: 
			# click the next button 
			next_el.click() 
			sleep(2) 
			# like the post 
			like_post()	 
			sleep(2)	
			next_el = next_post()		 
		except Exception as e: 
			print("The last post")  #When it reaches the end 
			break
		
def comment_post(message):
	sleep(2)
	#finds the comment's area and clicks on it
	comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
	comment.click()
	sleep(2)
	#Types the comment
	browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
	sleep(1)
	#Posts the comment
	browser.find_element_by_xpath("//button[contains(text(), 'Post')]").click()

def comment_till_the_end(): 
	next_el = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
	while(True): 
		# if next button is there then 
		try: 
			# click the next button 
			next_el.click() 
			sleep(2) 
			# comments on the post 
			comment_post(msg)	 
			sleep(2)	
			next_el = next_post()		 
		except Exception as e: 
			print("The last pose") #When it reaches the end 
			break
		


username = input("Enter the username of your account : ")
password = input("Enter the password of your account : ")
like_acc = input("Enter the Account name you want to spam likes : ")
msg = input("Enter the comment you want to spam : ")
exe_path = input("Enter the path of your driver : ")
global browser
browser = webdriver.Firefox(executable_path = exe_path) #Gets the geckodriver

my_bot = insta_bot(username,password) # logs in your account
my_bot.finduser(like_acc) # finds the account your looking for

#follow()		# use this to follow an account
#first_post() 	# use this to select the first post
#like_post() 	# use this to like only once
#like_till_the_end()	# use this to spam likes on all posts
#comment_post(msg)		# use this to comment on a post
#comment_till_the_end()	# use this to comment on all posts 

my_bot.quit(5)

