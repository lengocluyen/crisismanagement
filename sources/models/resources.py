from owlready2 import *
from .geoinfo import Geolocalisation
from .distance_map import *
from .utils import *
import os.path





class Campervan:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = instance.hasNbofAvailableLyingPlaces
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = instance.hasTotalNbofLyingPlaces
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Campervan(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'



class Minivan:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = instance.hasNbofAvailableLyingPlaces
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = instance.hasTotalNbofLyingPlaces
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Minivan(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'




class Van:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = 0
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = 0
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Van(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'





class SUV:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = 0
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = 0
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'SUV(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'



class Berline:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = 0
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = 0
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Berline(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'


class Minibus:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = 0
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = 0
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Minibus(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'
    

class Boat:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = instance.hasNbofAvailableLyingPlaces
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = instance.hasTotalNbofLyingPlaces
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Boat(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'
    
class Helicopter:

    def __init__(self, instance):
        self.name = instance.name
        self.nb_seats = instance.hasTotalNbofSeats
        self.speed = instance.hasSpeed
        self.state = instance.hasState
        self.available_lying_places = 0
        self.available_of_seats = int(instance.hasNbofAvailableSeats[0])
        self.lying_places = 0
        self.model_name = instance.hasModelName
        self.fuel_type = instance.fuelType
        self.geo_info = Geolocalisation(instance.hasGeolocalisationInformation)
        self.distance_estimate = []
        self.time_estimate = []
    
    def __repr__(self):
        return f'Helicopter(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'
    
class VehicleMngmt:

    def __init__(self, list_of_boat_ins, list_of_helicopter_ins, list_of_minibus_ins, list_of_berline_ins, list_of_suv_ins,
    list_of_van_ins, list_of_minivan_ins, list_of_campervan_ins, time_distance_files=None ):
        self.list_of_boats = self.binding_to_boat_instance(list_of_boat_ins)
        self.list_of_helipters = self.binding_to_helicopter_instance(list_of_helicopter_ins)
        self.list_of_minibus = self.binding_to_minibus_instance(list_of_minibus_ins)
        self.list_of_berlines = self.binding_to_berline_instance(list_of_berline_ins)
        self.list_of_suv = self.binding_to_suv_instance(list_of_suv_ins)
        self.list_of_van = self.binding_to_van_instance(list_of_van_ins)
        self.list_of_minivan = self.binding_to_minivan_instance(list_of_minivan_ins)
        self.list_of_campervan = self.binding_to_campervan_instance(list_of_campervan_ins)
        self.list_of_all_vehicles = self.list_of_vehicles()
        d_info =[] 
        if time_distance_files[0] is not None and os.path.exists(time_distance_files[0]):
            d_info = read_from_csv(time_distance_files[0])
        print("d_info", len(d_info))
        for line in d_info:
            if len(line) == len(self.list_of_all_vehicles):
                for i in range(0,len(self.list_of_all_vehicles)):
                    self.list_of_vehicles_in_object()[i].distance_estimate.append(line[i])
        t_info = []
        if time_distance_files[1] is not None and os.path.exists(time_distance_files[1]):
            t_info = read_from_csv(time_distance_files[1])
        for line in t_info:
            if len(line) == len(self.list_of_all_vehicles):
                for i in range(0,len(self.list_of_all_vehicles)):
                    self.list_of_vehicles_in_object()[i].time_estimate.append(line[i])
                    


    def add_distances_from_vehicle_to_rescuepoint(self, list_of_rescurepoint, city_name, save_path):
        openstreetmap = OpenStreetMap(city_name)
        d_table = []
        t_table = []
        for res_point in list_of_rescurepoint:
            destination = res_point.geo_info.coordinate
            d_row = []
            t_row = []
            for ins in self.list_of_minibus:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                print(res_point.name, ins.name)
                d_row.append(distance)
                t_row.append(time)
            for ins in self.list_of_suv:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                d_row.append(distance)
                t_row.append(time)
            for ins in self.list_of_berlines:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                d_row.append(distance)
                t_row.append(time)
            for ins in self.list_of_van:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                d_row.append(distance)
                t_row.append(time)
            for ins in self.list_of_minivan:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                d_row.append(distance)
                t_row.append(time)
            for ins in self.list_of_campervan:
                origine = ins.geo_info.coordinate
                distance = openstreetmap.get_distance(destination, origine, by="length")
                time = openstreetmap.get_distance(destination, origine, by="travel_time")
                ins.distance_estimate.append(distance)
                ins.time_estimate.append(time)
                d_row.append(distance)
                t_row.append(time)
            d_table.append(d_row)
            t_table.append(t_row)
        save_to_csv(d_table, os.path.join(save_path,"./distance.csv"))
        save_to_csv(t_table, os.path.join(save_path,"./time.csv"))
        return d_table, t_table
            
    def list_of_vehicles_in_object(self):
        
        items = [] #name, nb
        for ins in self.list_of_minibus:
            items.append(ins)
        for ins in self.list_of_suv:
            items.append(ins)
        for ins in self.list_of_berlines:
            items.append(ins)
        for ins in self.list_of_van:
            items.append(ins)
        for ins in self.list_of_minivan:
            items.append(ins)
        for ins in self.list_of_campervan:
            items.append(ins)
        #for ins in self.list_of_boats:
        #    items.append([ins.name, ins,  ins.available_of_seats])
        return items


    def list_of_vehicles(self):
        
        items = [] #name, nb
        for ins in self.list_of_minibus:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        for ins in self.list_of_suv:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        for ins in self.list_of_berlines:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        for ins in self.list_of_van:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        for ins in self.list_of_minivan:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        for ins in self.list_of_campervan:
            items.append([ins.name, ins,  ins.available_of_seats, ins.distance_estimate, ins.time_estimate])
        #for ins in self.list_of_boats:
        #    items.append([ins.name, ins,  ins.available_of_seats])
        return items
    
    def list_of_vehicles_by_distance_to_secure_points(self):
        result = []
        for item in self.list_of_vehicles():
            result.append(item[3])
        return result

    def list_of_vehicles_by_nb_of_seats(self):
        result = []
        for item in self.list_of_vehicles():
            result.append(item[2])
        return result

    def binding_to_campervan_instance(self, list_of_campervan_ins):
        rl_results = []
        for ins in list_of_campervan_ins:
            rl = Campervan(ins)
            rl_results.append(rl)
        return rl_results

    def binding_to_minivan_instance(self, list_of_minivan_ins):
        rl_results = []
        for ins in list_of_minivan_ins:
            rl = Minivan(ins)
            rl_results.append(rl)
        return rl_results

    def binding_to_van_instance(self, list_of_van_ins):
        rl_results = []
        for ins in list_of_van_ins:
            rl = Van(ins)
            rl_results.append(rl)
        return rl_results


    def binding_to_suv_instance(self, list_of_suv_ins):
        rl_results = []
        for ins in list_of_suv_ins:
            rl = SUV(ins)
            rl_results.append(rl)
        return rl_results


    def binding_to_berline_instance(self, list_of_berline_ins):
        rl_results = []
        for ins in list_of_berline_ins:
            rl = Berline(ins)
            rl_results.append(rl)
        return rl_results


    def binding_to_minibus_instance(self, list_of_minibus_ins):
        rl_results = []
        for ins in list_of_minibus_ins:
            rl = Minibus(ins)
            rl_results.append(rl)
        return rl_results

    def binding_to_helicopter_instance(self, list_of_helicopter_ins):
        rl_results = []
        for ins in list_of_helicopter_ins:
            rl = Helicopter(ins)
            rl_results.append(rl)
        return rl_results
    
    def binding_to_boat_instance(self, list_of_boat_ins):
        rl_results = []
        for ins in list_of_boat_ins:
            rl = Boat(ins)
            rl_results.append(rl)
        return rl_results
    
    def __repr__(self):
        str = ""
        for ins in self.list_of_boats:
            str += repr(ins) + "\n"
        for ins in self.list_of_helipters:
            str += repr(ins) + "\n"
        for ins in self.list_of_minibus:
            str += repr(ins) + "\n"
        for ins in self.list_of_berlines:
            str += repr(ins) + "\n"
        for ins in self.list_of_suv:
            str += repr(ins) + "\n"
        for ins in self.list_of_van:
            str += repr(ins) + "\n"
        for ins in self.list_of_minivan:
            str += repr(ins) + "\n"
        for ins in self.list_of_campervan:
            str += repr(ins) + "\n"
        return str