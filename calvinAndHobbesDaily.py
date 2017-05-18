"""
Downloads the Calvin and Hobbes comic strip for the day from www.gocomics.com.
Simply copy this script into a folder and run it where you want the comic strip to be downloaded. :)

Requires package beautifulsoup4. Install using command: pip install beautifulsoup4
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import datetime

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
headers = {'User-Agent': user_agent}

comic = 'calvinandhobbes'
dt = datetime.datetime.now().strftime("%Y/%m/%d")
url = 'http://www.gocomics.com/' + comic + '/' + dt   # Can be modified to URL of any comic on www.gocomics.com

filename = comic + '-' + datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'

req = Request(url, None, headers)

with urlopen(req) as response:
    html = response.read()

soup = BeautifulSoup(html, 'html.parser')
img_src = soup.find_all('picture', {'class': 'img-fluid item-comic-image'})[0].img['src']
urlretrieve(img_src, filename)  # Save file with `filename`
