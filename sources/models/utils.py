import os
import numpy as np 
from numpy import genfromtxt
from urllib.request import urlopen
import json

def get_coordinate_from_address(address):
    address = address.replace(" ", "+")
    #address = "35-39 Quai du Clos des Roses, 60200 Compiegne".replace(" ", "+")
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&polygon=1&addressdetails=1"
    response = urlopen(url)
    data_json = json.loads(response.read())
    x = data_json[0]["lat"]
    y = data_json[0]["lon"]
    return x, y

def save_to_csv(data, save_path):
    np_data = np.asarray(data)
    np_data.tofile(save_path, sep='|')

def read_from_csv(path_file, nb_of_secure_point=5):
    my_data = genfromtxt(path_file, delimiter='|')
    my_data = my_data.astype(int)
    my_data = np.split(my_data, nb_of_secure_point)
    new_result = []
    for item in my_data:
        sss = np.split(item, len(item)/2)
        new_result.append(sss)
    return new_result

