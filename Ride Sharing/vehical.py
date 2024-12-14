from abc import ABC

class Vehical(ABC):
    speed ={
        "car" : 50,
        "bike" : 60,
        "cng" : 15
    }
    def __init__(self,vehical_type,licence_plate,rate):
        self.vehical_type = vehical_type
        self.licence_plate = licence_plate
        self.rate = rate
class Car(Vehical):
    def __init__(self, vehical_type, licence_plate, rate):
        super().__init__(vehical_type, licence_plate, rate)

class Bike(Vehical):
    def __init__(self, vehical_type, licence_plate, rate):
        super().__init__(vehical_type, licence_plate, rate)