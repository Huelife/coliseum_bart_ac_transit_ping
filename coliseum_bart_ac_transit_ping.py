"""
coliseum_bart_ac_transit_ping.py: 
Scraping AC Transit API using Python to ping 
bus location at Coliseum Bart in Oakland
"""

import webbrowser

import requests
from requests.exceptions import HTTPError
from requests import get

latitude = 37.7537939
longitude = 122.197005
distance = 500
routeName = 805

api_key = input("API Key: ")
url = (f"https://api.actransit.org/transit/stops/{latitude}/{longitude}"
        "?distance={distance}&routeName={routeName}/?token={api_key}")

r = requests.get(url)
data = r.raw.read()

print(data)
