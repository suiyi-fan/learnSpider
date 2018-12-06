#coding=utf-8

import requests
from bs4 import BeautifulSoup
import chardet

def get_add(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.text,"html.parser")
    user_divs = soup.find_all('div',class_="user-statis user-block")
    #user_add = soup.body.div.div.div.div.ul.li
    for user_div in user_divs:
        user_adds = user_div.find_all('li')
    #user_add = soup.div.find_all('span')
        for user_add in user_adds:
            #print(user_add)
            if user_add.span is not None:
                print(user_add.span.get_text())
    print('end')
    #print(soup.find_all(text='故乡:'))

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/users/14588028/'
    get_add(url)