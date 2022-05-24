from owlready2 import *
from .geoinfo import Geolocalisation
from .distance_map import *
from .utils import *
import os.path

class RescuePoint:
    def __init__(self, rescue_point_instance):
        self.name = rescue_point_instance.name
        self.nb_of_person = int(rescue_point_instance.hasNbOfPerson[0])
        self.nb_of_disable_person = int(rescue_point_instance.hasNbofDisablePerson[0])
        self.priority_level = rescue_point_instance.hasPriorityLevel
        self.geo_info = Geolocalisation(rescue_point_instance.hasGeolocalisationInformation)
        self.distance_estimate_to_shelters = []
        self.time_estimate_to_shelters = []
    
    def __repr__(self):
        return f'RescuePoint(name:"{self.name}",nb_of_person:"{self.nb_of_person}",priority_level:"{self.priority_level}",{self.geo_info})'



class RescuePointMngmt:
    def __init__(self, list_of_rescue_point_instance, time_distance_files=None):
        self.list_of_rescue_point = self.binding_to_rescue_point_instance(list_of_rescue_point_instance)
        d_info =[] 
        if time_distance_files[0] is not None and os.path.exists(time_distance_files[0]):
            d_info = read_from_csv(time_distance_files[0])
        print("distance geolocation_shelters_info", len(d_info))
        for line in d_info:
            if len(line) == len(self.list_of_rescue_point):
                for i in range(0,len(self.list_of_rescue_point)):
                    self.list_of_rescue_point[i].distance_estimate_to_shelters.append(line[i])
        t_info = []
        if time_distance_files[1] is not None and os.path.exists(time_distance_files[1]):
            t_info = read_from_csv(time_distance_files[1])
        for line in t_info:
            if len(line) == len(self.list_of_rescue_point):
                for i in range(0,len(self.list_of_rescue_point)):
                    self.list_of_rescue_point[i].time_estimate_to_shelters.append(line[i])
    
    def binding_to_rescue_point_instance(self, list_of_rescue_point_instance):
        rl_results = []
        for ins in list_of_rescue_point_instance:
            rl = RescuePoint(ins)
            rl_results.append(rl)
        return rl_results
    
    def add_distances_from_rescuepoint_to_shelter(self, list_of_sheters, city_name, save_path):
        openstreetmap = OpenStreetMap(city_name)
        d_table = []
        t_table = []
        for shelter in list_of_sheters:
            destination = shelter.geo_info.coordinate
            d_row = []
            t_row = []
            for ins in self.list_of_rescue_point:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate_to_shelters.append(distance)
                ins.time_estimate_to_shelters.append(time)
                print(shelter.name, ins.name)
                d_row.append(distance)
                t_row.append(time)
            d_table.append(d_row)
            t_table.append(t_row)
        save_to_csv(d_table, os.path.join(save_path,"./distance_estimate_securepoint_to_shelters.csv"))
        save_to_csv(t_table, os.path.join(save_path,"./time_estimate_securepoint_to_shelters.csv"))
        return d_table, t_table

    def list_of_securepoint_by_nb_of_person(self):
        result = []
        for item in self.list_of_rescue_point:
            result.append([item.nb_of_person, item.nb_of_disable_person])
        return result

    def __repr__(self):
        str = ""
        for ins in self.list_of_rescue_point:
            str += repr(ins) + "\n"
        return str