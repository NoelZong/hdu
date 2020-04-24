import requests
import urllib
import time
import nltk
from urllib import request
from nltk import word_tokenize
from bs4 import BeautifulSoup


url = "https://www.crummy.com/nb/nb.cgi/view/nycb/lastmonth"
html = request.urlopen(url).read().decode('utf8')
print("flag1")
raw = BeautifulSoup(html, 'html.parser').get_text()
print("flag2")
tokens = word_tokenize(raw)
print(tokens)
