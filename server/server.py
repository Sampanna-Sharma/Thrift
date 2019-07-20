from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def search_web():
    product_name = request.args.get('ProductName')
    link =f"https://www.google.com/search?hl=en&as_q={product_name}+card&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=countryNP&as_qdr=all&as_sitesearch=&as_occt=title&safe=images&as_filetype=&as_rights="
    r = requests.get(link)
    # result = json.loads(r.text)
    return str(r.text)

if __name__ == "__main__":
    app.run(debug = True)

