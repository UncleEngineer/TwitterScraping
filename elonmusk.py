# elonmusk.py
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time



driverpath = r'C:\Users\Uncle Engineer\Desktop\ELON MUSK\chromedriver_win32\chromedriver.exe'

#hide google chrome

opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(driverpath,options=opt)


def TwitterPost(twitter_name):

	url = 'https://twitter.com/{}'.format(twitter_name) 

	driver.get(url)

	time.sleep(5)

	'''
	# Scrolling
	pixel = 10000

	for i in range(3):
		driver.execute_script("window.scrollTo(0, {})".format(pixel))
		time.sleep(3)
		pixel = pixel + 10000
	'''

	page_html = driver.page_source #print out html

	#print(page_html)
	data = soup(page_html, 'html.parser')

	posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})

	#print(posts)

	founddot = False

	allpost = []

	for p in posts:
		txt = p.text

		if founddot == True:
			allpost.append(txt)
			#print(txt)
			#print('--------------------')
			founddot = False

		if txt == '·':
			founddot = True
		

	return allpost




#################################

from songline import Sendline
token = 'XBl8ulCzgdiir5q4wzd48gd43TVxunOq71FGHRZDRHf'
messenger = Sendline(token)

#messenger.sendtext()


checktwitter = ['elonmusk','BillGates','cnnbrk','SpaceX']

for ct in checktwitter:
	texttoline = ''
	post = TwitterPost(ct)
	print('---------- {} ------------'.format(ct))
	texttoline += '---------- {} ------------\n'.format(ct)
	for p in post:
		print(p)
		texttoline += p + '\n\n' # texttoline = texttoline + p
		print('=====')
		
	messenger.sendtext(texttoline)

driver.close()




