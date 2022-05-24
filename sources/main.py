from curses.ascii import NUL
import os
from owlready2 import *
from models.resources import *
from models.rescuepoint import *
from models.shelter import *
from models.solvers import *



# Models and Data Path
kb_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/evacuation_models_instances.owl"
save_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/"

def load_models_and_data_from_file(data_path):
    kb = get_ontology(data_path).load()
    return kb

if __name__ == "__main__":
    print("###########")
    kb = load_models_and_data_from_file(kb_path)
    list_of_rescue_point_instance = kb.RescuePoint.instances()
    time_distance_files = [os.path.join(save_path, "distance_estimate_securepoint_to_shelters.csv"), os.path.join(save_path, "time_estimate_securepoint_to_shelters.csv")]
    list_of_rescue_point = RescuePointMngmt(list_of_rescue_point_instance, time_distance_files=time_distance_files)

    print("====List of Rescue point====")
    print(repr(list_of_rescue_point))

    list_of_shelter_instances = kb.Shelter.instances()
    list_of_shelters = ShelterMngmt(list_of_shelter_instances)
    print("====List of Shelter====")
    print(repr(list_of_shelters))

    print("")

    print("====List of Vehicle Resources====")
    list_of_boat_ins = kb.Boat.instances()
    list_of_helicopter_ins = kb.Helicopter.instances()
    list_of_minibus_ins = kb.Minibus.instances()
    list_of_berline_ins = kb.Berline.instances()
    list_of_suv_ins = kb.SUV.instances()
    list_of_van_ins = kb.Van.instances()
    list_of_minivan_ins = kb.Minivan.instances()
    list_of_campervan_ins = kb.Campervan.instances()
    time_distance_files = [os.path.join(save_path, "distance.csv"), os.path.join(save_path, "time.csv")]
    list_of_vehicles = VehicleMngmt(list_of_boat_ins, list_of_helicopter_ins, list_of_minibus_ins,
    list_of_berline_ins, list_of_suv_ins, list_of_van_ins, list_of_minibus_ins,
    list_of_campervan_ins, time_distance_files=time_distance_files)
    print(repr(list_of_vehicles))

    print("====Distance estimate====")
    # run it distance.csv and time.csv doesn't exist in the data and model directory
    # objective: get distance and time from vehicle to each secure point from OpenStreetMap data
    if os.path.exists(os.path.join(save_path,"distance.csv")) is False: 
        d_table, t_table = list_of_vehicles.add_distances_from_vehicle_to_rescuepoint(list_of_rescue_point.list_of_rescue_point,"Oise, France", save_path)
        print("d_table:", d_table)
    # objective get distance and time estimated  from the secure points to shelter by using OpenStreetMap
    # results are saved in distance_estimate_securepoint_to_shelters.csv and time_estimate_securepoint_to_shelters.csv
    if os.path.exists(os.path.join(save_path,"distance_estimate_securepoint_to_shelters.csv")) is False: 
        sp_d_table, sp_t_table = list_of_rescue_point.add_distances_from_rescuepoint_to_shelter(list_of_shelters.binding_to_shelter_instance,"Oise, France", save_path)
        print("sp_d_table:", sp_d_table)


    # case 1: Full vehicle for each secure point: total number of seats of all vehicle >= total person at all secure points
    # the priority level isn't used. it is not necessary.
    print("====Vehicle Recommendation====")
    csp_solver = CSPSolver(list_of_vehicles, list_of_rescue_point)
    csp_solver.csp_solver()
    # case 2: Limited vehicle: total number of seats of all vehicle < total person at all secure points
    # The priority is used to decide the ordre of secure points

