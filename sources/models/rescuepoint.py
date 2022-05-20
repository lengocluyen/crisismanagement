from owlready2 import *
from .geoinfo import Geolocalisation

class RescuePoint:
    def __init__(self, rescue_point_instance):
        self.name = rescue_point_instance.name
        self.nb_of_person = int(rescue_point_instance.hasNbOfPerson[0])
        self.priority_level = rescue_point_instance.hasPriorityLevel
        self.geo_info = Geolocalisation(rescue_point_instance.hasGeolocalisationInformation)
    
    def __repr__(self):
        return f'RescuePoint(name:"{self.name}",nb_of_person:"{self.nb_of_person}",priority_level:"{self.priority_level}",{self.geo_info})'



class RescuePointMngmt:
    def __init__(self, list_of_rescue_point_instance):
        self.list_of_rescue_point = self.binding_to_rescue_point_instance(list_of_rescue_point_instance)
    
    def binding_to_rescue_point_instance(self, list_of_rescue_point_instance):
        rl_results = []
        for ins in list_of_rescue_point_instance:
            rl = RescuePoint(ins)
            rl_results.append(rl)
        return rl_results
    

    def list_of_securepoint_by_nb_of_person(self):
        result = []
        for item in self.list_of_rescue_point:
            result.append(item.nb_of_person)
        return result

    def __repr__(self):
        str = ""
        for ins in self.list_of_rescue_point:
            str += repr(ins) + "\n"
        return str