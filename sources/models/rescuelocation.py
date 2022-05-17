from owlready2 import *
from .geoinfo import GeographicInformation

class RescueLocation:
    def __init__(self, rescue_location_instance):
        self.name = rescue_location_instance.name
        self.nb_of_person = int(rescue_location_instance.hasNbOfPerson[0])
        self.priority_level = rescue_location_instance.hasPriorityLevel
        self.geo_info = GeographicInformation(rescue_location_instance.hasGeographicalInformation)
    
    def __repr__(self):
        return f'RescueLocation(name:"{self.name}",nb_of_person:"{self.nb_of_person}",priority_level:"{self.priority_level}",{self.geo_info})'



class RescueLocationMngmt:
    def __init__(self, list_of_rescue_location_instance):
        self.list_of_rescue_location = self.binding_to_rescue_location_instance(list_of_rescue_location_instance)
    
    def binding_to_rescue_location_instance(self, list_of_rescue_location_instance):
        rl_results = []
        for ins in list_of_rescue_location_instance:
            rl = RescueLocation(ins)
            rl_results.append(rl)
        return rl_results
    

    def list_of_securelocation_by_nb_of_person(self):
        result = []
        for item in self.list_of_rescue_location:
            result.append(item.nb_of_person)
        return result

    def __repr__(self):
        str = ""
        for ins in self.list_of_rescue_location:
            str += repr(ins) + "\n"
        return str