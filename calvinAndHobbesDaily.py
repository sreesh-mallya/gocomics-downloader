"""
Downloads the Calvin and Hobbes comic strip for the day from www.gocomics.com.
Simply copy this script into a folder and run it where you want the comic strip to be downloaded. :)
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import datetime

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
headers = {'User-Agent': user_agent}

base_url = 'http://www.gocomics.com/calvinandhobbes/'   # Can be modified to URL of any comic on www.gocomics.com

today = datetime.datetime.now().strftime("%Y/%m/%d")

filename = datetime.datetime.now().strftime("%Y-%m-%d") + '.gif'   # Save downloaded file as <today's date>.gif

req = Request(base_url+today, None, headers)

with urlopen(req) as response:
    html = response.read()

soup = BeautifulSoup(html, 'lxml')
img_src = soup.find_all('picture', {'class': 'img-fluid item-comic-image'})[0].img['src']
urlretrieve(img_src, filename)  # Save file with `filename`
