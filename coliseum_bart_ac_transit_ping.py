"""
coliseum_bart_ac_transit_ping.py: 
Scraping AC Transit API using Python to ping 
bus location at Coliseum Bart in Oakland
"""

import webbrowser

import requests
from requests.exceptions import HTTPError
from requests import get

api_key = input("API Key: ")
url = ""

r = requests.get(url)
data = r.raw.read()

print(data)
