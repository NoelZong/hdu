from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import nltk
import csv

#base_url = "http://example.webscraping.com"
#his = ["/places/default/indexj"]
base_url = "https://www.crummy.com"
his = ["/nb/nb.cgi/view/nycb/lastmonth"]
def create_csv():
    path = "aa.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ["count","word"]
        csv_write.writerow(csv_head)
create_csv()

for i in range(2):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])
    

    text = soup.get_text(strip=True)
    tokens = [t for t in text.split()]
    freq = nltk.FreqDist(tokens)
    for key,val in freq.items():
        print(type(val), type(key))
        path  = "aa.csv"
        with open(path,'a+') as f:
            csv_write = csv.writer(f)
            data_row = [str(val),str(key)]
            csv_write.writerow(data_row)
    sub_urls = soup.find_all("a")
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()

