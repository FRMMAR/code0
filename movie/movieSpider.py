# _*_ coding: utf-8 _*_
#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time
from m1.models import M1Models

"""
get movie name from the page
get movie introduction from children page
"""

def get_page_txt(url):
    """
    get page text string
    """
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    r = requests.get(url, headers=headers)
    return r.text


def get_content(html, page):
    """
    get the content we want and save it
    """
#    output = """moviename:{}\nlink:{}\nrank{}\ninfo{}\nupdatetime{}\n----------\n"""
#    for output format
    soup = BeautifulSoup(html, 'html.parser')
    con_list = soup.find_all('a', class_="myui-vodlist__thumb lazyload")
    for i in con_list:
        title = i.get('title')  
        href = i.get('href')
        href = 'http://9ekk.com'+href
        rank = i.find('span',class_="pic-tag pic-tag-top").get_text().strip()
        info = parseInfo(href)
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        m1models = M1Models(title = title, content = info, link = href)
        m1models.save()

def parseInfo(url):
    """
    parse the content in children page
    """
    html = get_page_txt(url)
    soup = BeautifulSoup(html, 'html.parser')
    con = soup.find(class_="col-pd text-collapse content").get_text().strip().rstrip(".content img{ max-width: 100%;}")
#    print(con)
    return con   

def savedata(j):
    """
    get a series of pages for movie info
    """
    for i in range(j, j+5):
        url = 'http://9ekk.com/vodshow/dianying/page/{}.html'.format(i)
        html = get_page_txt(url)
        get_content(html, i)
        print(i, 'is saved')
        
if __name__ == '__main__':
    main()

