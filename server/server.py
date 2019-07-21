from flask import Flask, jsonify, request
import threading 
import sys
sys.path.insert(0,'../scraper')
from google_cse_scrape import google_scrape
from daraz_scrape import getdata as daraz_getdata
from bestdeals_scrape import getdata as bestdeals_getdata
from nepbay_scrape import getdata as nepbay_getdata
from sastodeal_scrape import getdata as sastodeal_getdata
app = Flask(__name__)


def extactor(link):
    if "daraz" in link:
        return daraz_getdata

    elif "bestdeals" in link:
        return bestdeals_getdata

    elif "sastodeal" in link:
        return sastodeal_getdata
    
    elif "nepbay" in link:
        return nepbay_getdata
    
    else:
        return lambda x: "None"


def extract_info(link,result):
    extractor_func = extactor(link)
    response = extractor_func(link)
    if response != "None":
        result.append(response)


@app.route('/',methods = ['GET'])
def search_web():
    result = []
    product_name = request.args.get('ProductName')
    links = google_scrape(product_name)
    threads = []
    for i, link in enumerate(links):
        print(link)
        if "?" in link:
            continue

        t = threading.Thread(target=extract_info, args=(link,result))
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()
        
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0")

