from curses.ascii import NUL
import os
from owlready2 import *
from models.resources import *



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
    print("List of Rescue Location:")
    print(repr(list_of_rescue_location))

