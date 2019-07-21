import requests
import json

key ="AIzaSyB-cRSraVQxHE3cEir_ZdPxVcX4osY8aEM"
def google_scrape(product_name):
    response = []
    url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx=007209971530152036224:dx3jaxmkzfs&cr=countryNP&q=allintitle:{product_name}"
    print(url)
    r =requests.get(url)
    print(r.text)
    result = json.loads(r.text)
    try:
        for item in result["items"]:
            response.append(item["link"])
    
    except:
        print("no result for the search term")
    
    return response
