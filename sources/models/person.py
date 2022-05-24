from owlready2 import *

class Driver:
    def __init__(self, driver_instance):
        ins = driver_instance[0]
        self.phone_number = ins.hasPhoneNumber
        self.age = ins.hasAge
        self.address = ins.hasAddress
        self.name = ins.hasName
        self.sex = ins.hasSex

    def __repr__(self):
        return f'Driver(name:"{self.name}" age:"{self.age}",sex:"{self.sex}",phone:"{self.phone_number}",Address:"{self.address}")'
