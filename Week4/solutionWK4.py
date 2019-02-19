import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
listSum = []


for tag in tags:
    listSum.append(int(tag.string))

print('Sum: ' + str(sum(listSum)))