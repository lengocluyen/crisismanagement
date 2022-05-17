from owlready2 import *

class GeographicInformation:
    def __init__(self, geoinfo_instance):
        self.coordinate = geoinfo_instance[0].hasCoordinates
        self.longtitude = geoinfo_instance[0].hasLongtitude
        self.latitude = geoinfo_instance[0].hasLatitude
        self.location_name = geoinfo_instance[0].hasLocationName

    def __repr__(self):
        return f'GeographicInformation(coord:"{self.coordinate}",long:"{self.longtitude}",lat:"{self.latitude}",location:"{self.location_name}")'
