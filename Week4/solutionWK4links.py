import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL - ')
html = urllib.request.urlopen(url, 'html.parser')