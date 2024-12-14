from ride import *
from user import *
from vehical import *

jatra = Ride_sharing("Jatra")
rider1 = Rider("Fahim","fahim@gmail.com",1234,"Baridhara",2000)
jatra.add_rider(rider1)
rider2 = Rider("Kawshik","Jaihok@gmail.com",1236,"Malibag",1500)
jatra.add_rider(rider1)
driver1 = Driver("Mizan","mizan@gmail.com",1235,"Notunbazar")
jatra.add_driver(driver1)
rider2.ride_request(jatra,"uttora","car")
rider2.show_current_ride()
driver1.rech_destination(rider2.current_ride)
# rider2.show_current_ride()
print(jatra)
rider2.ride_request(jatra,"uttora","car")