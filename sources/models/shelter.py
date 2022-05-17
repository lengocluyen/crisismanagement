from owlready2 import *
from .geoinfo import GeographicInformation


    

class Shelter:
    def __init__(self, shelter_instance):
        self.name = shelter_instance.name
        self.capacity = shelter_instance.hasCapacity
        self.geo_info = GeographicInformation(shelter_instance.hasGeographicalInformation)
    
    def __repr__(self):
        return f'Shelter(name:"{self.name}",capacity:"{self.capacity}",{self.geo_info})'


class ShelterMngmt:
    def __init__(self, list_of_shelter_instances):
        self.list_of_shelters = self.binding_to_shelter_instance(list_of_shelter_instances)
    
    def binding_to_shelter_instance(self, list_of_shelter_instances):
        rl_results = []
        for ins in list_of_shelter_instances:
            rl = Shelter(ins)
            rl_results.append(rl)
        return rl_results
    
    def __repr__(self):
        str = ""
        for ins in self.list_of_shelters:
            str += repr(ins) + "\n"
        return str