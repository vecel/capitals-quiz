import json
import requests
from googletrans import Translator, constants

translator = Translator()

def to_polish(text: str) -> str:
    return translator.translate(text, src = "en", dest = "pl", timeout = 3).text

continents_translations = {
    "Europe": "Europa",
    "South America": "Ameryka Południowa",
    "Asia": "Azja",
    "Oceania": "Australia i Oceania",
    "North America": "Ameryka Północna",
    "Africa": "Afryka",
    "Antarctica": "Antarktyda"
}

url = 'https://parseapi.back4app.com/classes/Country?limit=99999999999&include=continent&keys=name,capital,continent,continent.name'
headers = {
    'X-Parse-Application-Id': 'mxsebv4KoWIGkRntXwyzg6c6DhKWQuit8Ry9sHja', # This is the fake app's application id
    'X-Parse-Master-Key': 'TpO0j3lG2PmEVMXlKYQACoOXKQrL3lwM0HwR9dbH' # This is the fake app's readonly master key
}
raw_data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need

CAPITALS = {}

for i in raw_data["results"]:
    continent = continents_translations[i["continent"]["name"]]
    country = i["name"]
    capital = i["capital"]
    
    if continent not in CAPITALS:
        CAPITALS[continent] = {}
    
    CAPITALS[continent].update({country: capital})

# print(json.dumps(CAPITALS, indent=2))
