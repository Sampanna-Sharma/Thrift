import bs4 as bs
import requests


url = "https://www.google.com/search?hl=en&as_q=buy+sound+card&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=countryNP&as_qdr=all&as_sitesearch=&as_occt=title&safe=images&as_filetype=&as_rights="
def scrape(url):
    r = requests.get(url)
    # print(r.text)
    soup = bs.BeautifulSoup(r.text,'lxml')

    
    print(headings)

    # print(headings)
scrape(url)