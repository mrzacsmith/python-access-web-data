import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Igore SSLcertificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get URL from user
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

# This will print the entire web page showing all html and data
# print(html)

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))