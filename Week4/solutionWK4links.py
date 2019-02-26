
from bs4 import BeautifulSoup
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter your start url: ')
count = input('Enter your count: ')
position = input('Enter your position: ')

for i in range(int(count)):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	number = 0
	for tag in tags:
		number += 1
		if number == int(position):
			url = tag.get('href')
			if i == int(count)-1:
				print(tag.contents[0])
			break