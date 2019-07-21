import re
import csv
import requests

from bs4 import BeautifulSoup


def getprice(soup, c):
    try:
        ret = soup.find('div', class_=c).text.strip()
        return ret
    except(AttributeError):
        None


def gettitle(soup, c):
    try:
        ret = soup.find(class_=c).text
        return ret
    except(AttributeError):
        None


def getrating(soup, d='div', c='score'):
    try:
        ret = soup.find(d, class_=c).text
        return ret
    except(AttributeError):
        None


def getcomment(soup, d='div', c='content'):
    try:
        ret = soup.find(d, class_=c).text
        return ret
    except(AttributeError):
        None


def getdata(url):
    d = dict()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    price = getprice(soup, 'PriceArea')
    title = gettitle(soup, 'ProdDetailTitle')
    rating = getrating(soup, 'div', 'score')
    comment = [getcomment(i, 'div', 'content') for i in soup.find_all('div', class_='item-content')]
    image_link = soup.find('div', class_='MainImage').find('img', class_='xzoom')['src']
    d['nepbay'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'image_link': image_link,'url':url}
    return d
