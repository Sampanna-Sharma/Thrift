import requests
import json

key ="AIzaSyAI5RjkaHpSmiRNjrnzsQZImfzAXYLyEO8"
url = "https://www.googleapis.com/customsearch/v1?key="+key+"&cx=007209971530152036224:dx3jaxmkzfs&cr=countryNP&q=allintitle: buy usb 3.0"
print(url)
r =requests.get(url)
print(r.text)
# data = json.loads(r.text)
# links = data.items
