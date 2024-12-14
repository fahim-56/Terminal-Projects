from abc import ABC,abstractmethod
from ride import Ride_Request,Ride_Matching
class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid,current_location,current_balance):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.walet = current_balance
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider : {self.name} Phone Email : {self.email}")

    def cash_in(self,amount):
        if amount > 0 :
            self.walet += amount
        else:
            print("Amount is less than 0")
    
    def update_location(self,current_location):
        self.current_location = current_location

    def ride_request(self,ride_sharing, destination,vehicle_type):
        request = Ride_Request(self,destination)
        ride_matching = Ride_Matching(ride_sharing.drivers)
        ride = ride_matching.finding_Driver(request,vehicle_type)
        if ride == None:
            print("No driver availavble now!")
            return
        self.current_ride = ride
        ride.rider = self
        print("Ride confiremd !")

    def show_current_ride(self):
        print(f"Riding details : {self.current_ride}")

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.walet = 0

    def display_profile(self):
        print(f"Driver name : {self.name}  Email : {self.email}")

    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self)
    
    def rech_destination(self,ride):
        ride.end_ride()
       