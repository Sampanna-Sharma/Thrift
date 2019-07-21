import re
import csv
import requests

from bs4 import BeautifulSoup


def getprice(soup, c):
    try:
        ret = soup.find('div', class_=c).find('p', class_='dprice').find_all('span')[3].text
        return ret
    except(AttributeError):
        None


def gettitle(soup):
    try:
        ret = soup.find('title').text.split('|')[0]
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

urls = ['https://smartdoko.com/shop/fantech-gaming-mouse-x5s-zeus']


def getdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    price = getprice(soup, 'product-information')
    title = gettitle(soup)
    rating = getrating(soup, 'div', 'score')
    comment = [getcomment(i, 'div', 'content') for i in soup.find_all('div', class_='item-content')]
    image_link = soup.find('div', id='surround').find('img', class_='cloudzoom')['src']
<<<<<<< HEAD
    d['smartdoko'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'image_link': image_link, 'url' : url}
=======
    d['nepbay'] = {'title': title, 'price': price, 'rating': rating, 'comment': comment, 'image_link': image_link}
>>>>>>> 9caf55906f41812fc2b4d050d4765ac2db5d12b2
    return d


print(getdata(urls[0]))
