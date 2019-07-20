from flask import Flask, jsonify, request

import sys
sys.path.insert(0,'../scraper')
from google_cse_scrape import google_scrape
from daraz_scrape import getdata as daraz_getdata
from bestdeals_scrape import getdata as bestdeals_getdata
from nepbay_scrape import getdata as nepbay_getdata
from sastodeal_scrape import getdata as sastodeal_getdata
app = Flask(__name__)


@app.route('/',methods = ['GET'])
def search_web():
    product_name = request.args.get('ProductName')
    result = dict()
    links = google_scrape(product_name)
    for i, link in enumerate(links):
        print(link)
        if "?" in link:
            continue
        if "daraz" in link:
            response = daraz_getdata(link)
            result[str(i)] = response
        
        elif "sastodeal" in link:
            response = sastodeal_getdata(link)
            result[str(i)] = response
        
        elif "bestdeals" in link:
            response = bestdeals_getdata(link)
            result[str(i)] = response
        
        elif "nepbay" in link:
            response = nepbay_getdata(link)
            result[str(i)] = response
        
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0")

