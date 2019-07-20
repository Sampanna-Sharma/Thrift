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

