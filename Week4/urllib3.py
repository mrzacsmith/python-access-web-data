import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')

for lines in fhand:
    print(lines.decode().strip())