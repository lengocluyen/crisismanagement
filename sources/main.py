from curses.ascii import NUL
import os
from owlready2 import *
from models.resources import *
from models.rescuepoint import *
from models.shelter import *
from models.recommand_engine import *



# Models and Data Path
kb_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/evacuation_models_instancesv1.owl"
save_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/"
kb = get_ontology(kb_path).load()



def initial_resouces():
    # get rescue point from user interface
    list_of_rescue_point = api_get_secure_point_infos(number_securepoints=2, \
    addresses=["35-39 Quai du Clos des Roses, 60200 Compiegne, France","46 Rue de l'Oise, 60200 Compiegne, France" ], \
    priority_levels=[1,2],nb_persons=[100, 200], nb_disable_persons=[5, 3])

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
        #print("d_table:", d_table)
    # objective get distance and time estimated  from the secure points to shelter by using OpenStreetMap
    # results are saved in distance_estimate_securepoint_to_shelters.csv and time_estimate_securepoint_to_shelters.csv
    if os.path.exists(os.path.join(save_path,"distance_estimate_securepoint_to_shelters.csv")) is False: 
        sp_d_table, sp_t_table = list_of_rescue_point.add_distances_from_rescuepoint_to_shelter(list_of_shelters.list_of_shelters,"Oise, France", save_path)
        #print("sp_d_table:", sp_d_table)
    else:
        print("Distance estimated are loaded from files")
    return list_of_rescue_point, list_of_shelters, list_of_vehicles

# [number_securepoints,address, priority_levels, nb_persons, nb_disable_persons]
# example[number_securepoints=2, addresses=[Ad1, Ad2], priority_levels=[1, 2],nb_persons=[100,200],nb_disable_persons=[5,1]]
def api_get_secure_point_infos(number_securepoints, \
    addresses=[], priority_levels=[],nb_persons=[], nb_disable_persons=[]):
    list_of_rescue_point_instance = []
    for i in range(number_securepoints):
        rescue_point = RescuePoint(rescue_point_instance=None, address=addresses[i], priority_level= priority_levels[i], \
        nb_person=nb_persons[i], nb_disable_person=nb_disable_persons[i])
        list_of_rescue_point_instance.append(rescue_point)

    time_distance_files = [os.path.join(save_path, "distance_estimate_securepoint_to_shelters.csv"), os.path.join(save_path, "time_estimate_securepoint_to_shelters.csv")]
    list_of_rescue_point = RescuePointMngmt(list_of_rescue_point_instance, time_distance_files=time_distance_files, from_user=True)
    return list_of_rescue_point
    
    
# return
# name of vehicles, driver, addresse of the vehicles, 
# # number of the places availbale of vehicles, distance and time vehicle and securepoint
def api_post_a_recommenation():
    list_of_rescue_point, list_of_shelters, list_of_vehicles = initial_resouces()
    print("====Vehicle Recommendation====")
    cityname = "Oise, France"
    recommand_engine = RecommandEngine(list_of_vehicles, list_of_rescue_point, list_of_shelters,cityname)
    generateur, x, objective = recommand_engine.generating_recommand(dynamic_resource=True)
    # print and return la meuilleure proposition
    result = recommand_engine.best_optimal_recommand(generateur,x, objective)
    print(result)
    return result

def api_post_other_recommends(number=1):
    list_of_rescue_point, list_of_shelters, list_of_vehicles = initial_resouces()
    print("====Vehicle Recommendation====")
    cityname = "Oise, France"
    recommand_engine = RecommandEngine(list_of_vehicles, list_of_rescue_point, list_of_shelters,cityname)
    generateur, x, objective = recommand_engine.generating_recommand(dynamic_resource=True)
    # print and return the {number} propositions
    nb_of_recommend = number
    result = recommand_engine.vehicle_resource_recommand(generateur, x, objective, nb_of_recommend)
    print(result)
    return result

if __name__ == "__main__":
    print("###########")
    #api_post_a_recommenation()
    api_post_other_recommends(number=2)
    """
    # from info securepoint from ontology
    list_of_rescue_point_instance = kb.RescuePoint.instances()
    time_distance_files = [os.path.join(save_path, "distance_estimate_securepoint_to_shelters.csv"), os.path.join(save_path, "time_estimate_securepoint_to_shelters.csv")]
    list_of_rescue_point = RescuePointMngmt(list_of_rescue_point_instance, time_distance_files=time_distance_files)
    
    # get rescue point from user interface
    list_of_rescue_point = api_get_secure_point_infos(number_securepoints=2, \
    addresses=["35-39 Quai du Clos des Roses, 60200 Compiegne, France","46 Rue de l'Oise, 60200 Compiegne, France" ], \
    priority_levels=[1,2],nb_persons=[100, 200], nb_disable_persons=[5, 3])

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
        #print("d_table:", d_table)
    # objective get distance and time estimated  from the secure points to shelter by using OpenStreetMap
    # results are saved in distance_estimate_securepoint_to_shelters.csv and time_estimate_securepoint_to_shelters.csv
    if os.path.exists(os.path.join(save_path,"distance_estimate_securepoint_to_shelters.csv")) is False: 
        sp_d_table, sp_t_table = list_of_rescue_point.add_distances_from_rescuepoint_to_shelter(list_of_shelters.list_of_shelters,"Oise, France", save_path)
        #print("sp_d_table:", sp_d_table)
    else:
        print("Distance estimated are loaded from files")


    #  for each secure point: total number of seats of all vehicle >= total person at all secure points
    # the priority level isn't used. it is not necessary.
    print("====Vehicle Recommendation====")
    recommand_engine = RecommandEngine(list_of_vehicles, list_of_rescue_point)
    generateur, x, objective = recommand_engine.generating_recommand(dynamic_resource=True)
    # la meuilleure proposition
    recommand_engine.best_optimal_recommand(generateur,x, objective)
    # generating other recommands
    nb_of_recommend = 2
    recommand_engine.vehicle_resource_recommand(generateur, x, objective, nb_of_recommend)
    """
