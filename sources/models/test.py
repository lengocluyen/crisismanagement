import numpy as np
import osmnx as ox
from urllib.request import urlopen
import json


address = "35-39 Quai du Clos des Roses, 60200 Compiegne".replace(" ", "+")
url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&polygon=1&addressdetails=1"
response = urlopen(url)

data_json = json.loads(response.read())
print(data_json[0]["lat"])
print(data_json[0]["lon"])