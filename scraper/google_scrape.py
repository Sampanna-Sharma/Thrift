import bs4 as bs
import requests
import re


def scrape(url):
    link = []
    r = requests.get(url)
    # print(r.text)
    soup = bs.BeautifulSoup(r.text, 'lxml')
    #urls = re.findall('^(http|https)://', r.text)
    # print(urls)
    data = soup.find_all('div', {'class': 'jfp3ef'})
    for dat in data:
        for links in dat.find_all('a'):
            a = links["href"].split('=')[1]
            # print(a)
            try:
                if "http" in a:
                    link.append(a.split('&')[0])
            except:
                pass
    return link


