import re
import csv
import requests

from bs4 import BeautifulSoup


def getprice(soup, c='pdp-product-price', s='span'):
    try:
        ret = soup.find('p', class_=c).find(s).text[3:]
        return ret
    except(AttributeError):
        None


def gettitle(soup, title='title'):
    try:
        ret = soup.find(title).text.split('|')[0]
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


<<<<<<< HEAD
=======

>>>>>>> 9caf55906f41812fc2b4d050d4765ac2db5d12b2
def getdata(url):
    d = dict()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    price = getprice(soup, 'price', 'span')
    title = gettitle(soup, 'title')
    rating = getrating(soup, 'div', 'score')
    comment = [getcomment(i, 'div', 'content') for i in soup.find_all('div', class_='item-content')]
    d['bestdeals'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'url' : url}
    return d
