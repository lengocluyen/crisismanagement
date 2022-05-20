from owlready2 import *

class Driver:
    def __init__(self, driver_instance):
        self.phone_number = driver_instance.hasPhoneNumber
        self.age = driver_instance.hasAge
        self.address = driver_instance.hasAddress
        self.name = driver_instance.hasName
        self.sex = driver_instance.hasSex

    def __repr__(self):
        return f'Driver(name:"{self.name}" age:"{self.age}",sex:"{self.sex}",phone:"{self.phone_number}",Address:"{self.address}")'
