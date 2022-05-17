from owlready2 import *
# Models and Data Path
kb_path = "/home/lengocluyen/projects/crisis_management/crisismanagement/ontology_models/evacuation_models_instances.owl"

onto = get_ontology(kb_path).load()

with onto:
    class Location(Thing): pass

    class Resource(Thing): pass

    class Vehicle (Thing): pass

    class Driver (Thing): pass
    