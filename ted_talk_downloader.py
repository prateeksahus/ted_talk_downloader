# Author: Prateek sahu
import requests

from bs4 import BeautifulSoup

import re

import sys

# to take the url as a command line argument
if len(sys.argv)>1:
    url = sys.argv[1]
else:
    sys.exit('Error: Enter a valid ted talk url')

# url = '' Enter url directly to download from code

r = requests.get(url)

print('Download about to start')

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.find_all('script'):
    if (re.search('talkPage.init', str(val))) is not None:
        result = str(val)

file_name = re.search(r'"slug":"\w+', result).group()[8:] + '.mp4'

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print('Downloading video from ... '+mp4_url)

print('Storing video in .... ' + file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

print('Download finished')