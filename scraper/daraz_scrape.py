import re
import csv
import requests

from bs4 import BeautifulSoup
import pandas as pd


def getprice(soup, d='div', c='pdp-product-price', s='span'):
    try:
        ret = soup.find(d, class_=c).find(s).text
        return ret
    except(AttributeError):
        None


def gettitle(soup, title='title'):
    try:
        ret = soup.find(title).text.split(':')[0]
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


d = dict()

urls = ['https://www.daraz.com.np/products/yunteng-combo-of-1288-selfie-stick-with-monopod-yt-228-tripod-i412207-s15304776.html?spm=a2a0e.searchlistcategory.list.1.5d9f104cJs1c0N&search=1', 'https://www.daraz.com.np/products/xo-s21-extreme-bass-in-ear-earphone-i100234623-s1020488869.html?spm=a2a0e.searchlistcategory.list.1.8af43ae7ZU1oq5&search=1', 'https://www.daraz.com.np/products/abc-5-port-multiplug-i113647-s723233.html']


def getdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    price = getprice(soup, 'div', 'pdp-product-price', 'span')
    title = gettitle(soup, 'title')
    rating = getrating(soup, 'div', 'score')
    comment = [getcomment(i, 'div', 'content') for i in soup.find_all('div', class_='item-content')]
    image_link = soup.find('img', class_='pdp-mod-common-image gallery-preview-panel__image')['src']
    d['daraz'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'image_link': image_link}
    return d


# for url in urls:
print(getdata(urls[0]))

# print(r.text)
# x = r.find_all('div', class_='pdp-mod-product-badge-wrapper')
# print(x.text)
