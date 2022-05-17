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
    print(list(kb.classes()))
    #print(list(kb.individuals()))
    vehicle = NUL
    for c in kb.classes():
        if c.name == "Vehicle":
            vehicle = c
    print(list(vehicle.subclasses()))
    print(kb.base_iri)