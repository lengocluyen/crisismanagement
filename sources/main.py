from curses.ascii import NUL
import os
from owlready2 import *
from models.resources import *
from models.rescuelocation import *
from models.shelter import *
from models.solvers import *



# Models and Data Path
kb_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/evacuation_models_instances.owl"


def load_models_and_data_from_file(data_path):
    kb = get_ontology(data_path).load()
    return kb

if __name__ == "__main__":
    print("###########")
    kb = load_models_and_data_from_file(kb_path)
    list_of_rescue_location_instance = kb.RescueLocation.instances()
    list_of_rescue_location = RescueLocationMngmt(list_of_rescue_location_instance)

    print("====List of Rescue Location====")
    print(repr(list_of_rescue_location))

    list_of_shelter_instances = kb.Shelter.instances()
    list_of_shelters = ShelterMngmt(list_of_shelter_instances)
    print("====List of Shelter====")
    print(repr(list_of_shelters))


    print("====List of Vehicle Resources====")
    list_of_boat_ins = kb.Boat.instances()
    list_of_helicopter_ins = kb.Helicopter.instances()
    list_of_minibus_ins = kb.Minibus.instances()
    list_of_sedan_ins = kb.Sedan.instances()
    list_of_suv_ins = kb.SUV.instances()
    list_of_van_ins = kb.Van.instances()
    list_of_minivan_ins = kb.Minivan.instances()
    list_of_campervan_ins = kb.Campervan.instances()
    list_of_vehicles = VehicleMngmt(list_of_boat_ins, list_of_helicopter_ins, list_of_minibus_ins,
    list_of_sedan_ins, list_of_suv_ins, list_of_van_ins, list_of_minibus_ins,
    list_of_campervan_ins)
    print(repr(list_of_vehicles))


    print("====Vehicle Recommendation====")
    csp_solver = CSPSolver(list_of_vehicles, list_of_rescue_location)
    csp_solver.csp_solver()
