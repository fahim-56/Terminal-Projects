from datetime import datetime
from vehical import *

class Ride_sharing:
    def __init__(self,company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)
        
    def add_driver(self,driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"{self.company_name} Company has :\nRider : {len(self.riders)}\nDriver : {len(self.drivers)}"

class Ride:
    def __init__(self,start_location, end_location,vehical):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimited_fare = self.calculate_fare(vehical=vehical.vehical_type)
        self.vehical = vehical
    
    def set_driver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.walet -= self.estimited_fare
        self.driver.walet += self.estimited_fare

    def calculate_fare(self,vehical):
        destination = 10
        fare_per_km = {
            "car" : 100,
            "bike" : 30,
            "cng" : 20
        }
        return destination * fare_per_km.get(vehical)

    def __repr__(self):
        if self.end_time== None:
            return f"\nRider :{self.rider.name} \nDriver : {self.driver.name}\nStart time : {self.start_time} from {self.start_location}\nEnd time : going to {self.end_location} on {self.vehical.vehical_type}"
        return f"\nRider :{self.rider.name} \nDriver : {self.driver.name}\nStart time : {self.start_time} from {self.start_location}\nEnd time : {self.end_time} at {self.end_location}"

class Ride_Request:
    def __init__(self,rider,end_location):
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __init__(self, drivers):
        self.available_drivers = drivers
    
    def finding_Driver(self,ride_request,vehical_type):
        if len(self.available_drivers)>0:
            print("Looking for drivers...")
            driver = self.available_drivers[0]
            self.available_drivers.pop()
            if vehical_type == "car":
                vehical = Car("car","1234",1000)
            elif vehical_type == "bike":
                vehical = Bike("bike","0987",500)
            ride = Ride(ride_request.rider.current_location,ride_request.end_location,vehical)
            driver.accept_ride(ride)
            return ride