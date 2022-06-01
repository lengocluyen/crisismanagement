from owlready2 import *
from .utils import get_coordinate_from_address
class Geolocalisation:
    def __init__(self, geoinfo_instance=None, address=None):
        if geoinfo_instance is not None:
            self.coordinate = geoinfo_instance[0].hasCoordinates
            self.longtitude = geoinfo_instance[0].hasLongtitude
            self.latitude = geoinfo_instance[0].hasLatitude
            self.location_name = geoinfo_instance[0].hasLocationName
        else:
            x, y = get_coordinate_from_address(address)
            self.coordinate = f"{x}, {y}"
            self.longtitude = x
            self.latitude = y
            self.location_name = address

    def __repr__(self):
        return f'Geolocalisation(coord:"{self.coordinate}",long:"{self.longtitude}",lat:"{self.latitude}",location:"{self.location_name}")'
