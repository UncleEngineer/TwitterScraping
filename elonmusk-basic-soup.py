# elonmusk.py
from selenium import webdriver
from bs4 import BeautifulSoup as soup

rawdata = '''
<!DOCTYPE html>
<html>
<head>
	<title>UNCLE ENGINEER</title>
</head>
<body>

	<div class="testdiv">
		<h1>ELON MUSK</h1>
	</div>

</body>
</html>
'''

data = soup(rawdata,'html.parser')

print(data.title.text)

print(data.h1.text)