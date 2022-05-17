from owlready2 import *
from .geoinfo import GeographicInformation



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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
    def __repr__(self):
        return f'SUV(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'



class Sedan:

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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
    def __repr__(self):
        return f'Sedan(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'


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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
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
        self.geo_info = GeographicInformation(instance.hasGeographicalInformation)
    
    def __repr__(self):
        return f'Helicopter(name:"{self.name}", state = "{self.state}",available_lying_places:"{self.available_lying_places}",available_of_seats:"{self.available_of_seats}",{self.geo_info})'
    
class VehicleMngmt:

    def __init__(self, list_of_boat_ins, list_of_helicopter_ins, list_of_minibus_ins, list_of_sedan_ins, list_of_suv_ins,
    list_of_van_ins, list_of_minivan_ins, list_of_campervan_ins ):
        self.list_of_boats = self.binding_to_boat_instance(list_of_boat_ins)
        self.list_of_helipters = self.binding_to_helicopter_instance(list_of_helicopter_ins)
        self.list_of_minibus = self.binding_to_minibus_instance(list_of_minibus_ins)
        self.list_of_sedans = self.binding_to_sedan_instance(list_of_sedan_ins)
        self.list_of_suv = self.binding_to_suv_instance(list_of_suv_ins)
        self.list_of_van = self.binding_to_van_instance(list_of_van_ins)
        self.list_of_minivan = self.binding_to_minivan_instance(list_of_minivan_ins)
        self.list_of_campervan = self.binding_to_campervan_instance(list_of_campervan_ins)


    def list_of_vehicles(self):
        
        items = [] #name, nb
        for ins in self.list_of_minibus:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_suv:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_sedans:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_van:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_minivan:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_campervan:
            items.append([ins.name, ins,  ins.available_of_seats])
        for ins in self.list_of_boats:
            items.append([ins.name, ins,  ins.available_of_seats])
        return items
    
    def list_of_vehicles_ny_nb_of_seats(self):
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


    def binding_to_sedan_instance(self, list_of_sedan_ins):
        rl_results = []
        for ins in list_of_sedan_ins:
            rl = Sedan(ins)
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
        for ins in self.list_of_sedans:
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