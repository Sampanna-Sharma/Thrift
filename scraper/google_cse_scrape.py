import requests
import json

key ="AIzaSyAI5RjkaHpSmiRNjrnzsQZImfzAXYLyEO8"
def google_scrape(product_name):
    response = []
    url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx=007209971530152036224:dx3jaxmkzfs&cr=countryNP&q=allintitle:{product_name}"
    print(url)
    r =requests.get(url)
    result = json.loads(r.text)
    for item in result["items"]:
        response.append(item["link"])
    
    return response
