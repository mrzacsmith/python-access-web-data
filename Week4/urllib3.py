import urllib.request, urllib.parse, urllib.error

url = 'http://www.simplesite.com/'

fhand = urllib.request.urlopen(url)

for lines in fhand:
    print(lines.decode().strip())