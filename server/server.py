from flask import Flask, jsonify, request

import sys
sys.path.insert(0,'../scraper')
from google_scrape import scrape
from daraz_scrape import getdata
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def search_web():
    product_name = request.args.get('ProductName')
    result = []
    links =f"https://www.google.com/search?hl=en&as_q={product_name}&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=countryNP&as_qdr=all&as_sitesearch=&as_occt=title&safe=images&as_filetype=&as_rights="
    links = scrape(links)
    for link in links:
        if "daraz" in link:
            response = getdata(link)
            result.append(response)
    return str(result)

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0")

