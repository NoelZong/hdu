import requests
import time
from bs4 import BeautifulSoup
import nltk

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_enconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "


def get_content(url):

    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 把需要爬取信息的网页下载到本地
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')
    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    filename = "soup.txt"
    with open(filename, 'wb+') as f:
        f.write(soup.encode('utf-8'))
    liTags = soup.find_all("td")
    #liTags = soup.find_all("li")
    print(liTags)
    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            comment['title'] = li.find(
                'a').text.strip()
            comment['link'] = "http://example.webscraping.com" + \
                li.find('a')['href']
            soup_word = BeautifulSoup(comment['link'], features='lxml')
            print(soup_word)
            text = soup_word.get_text(strip=True)     
            tokens = [t for t in text.split()]     
            freq = nltk.FreqDist(tokens)     
            for key,val in freq.items(): 
                comment['value'] = str(val)
                comment['word'] = str(key)         
            
            #comment['time'] = li.find(
                #'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            #comment['replyNum'] = li.find(
                #'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('ERROR')

    return comments


def Out2File(dict):
    with open('TTBT.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 数量：{} \t 词：{} \n'.format(
            #f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['value'], comment['word']))
                #comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('The current page is crawled')


def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '/' + str(i))
    print('download success')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('data saved')


#base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
base_url = 'http://example.webscraping.com/places/default/index'
# 设置需要爬取的页码数量
deep = 3

if __name__ == '__main__':
    main(base_url, deep)
