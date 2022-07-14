from car import Car
from driver import Driver
from payment import Payment
from rute import Rute
from user import User


class Trip(Car, User, Driver, Rute, Payment):
    idTrip         = int
    
    
    def __init__(self, idTrip, idUser, idDriver, star, end, KmDistance, typePayment, ammount, date, licence, driver ):
        super().__init__(id, idTrip, idUser, idDriver, star, end, KmDistance, typePayment, ammount, date, licence, driver)
        self.idTrip    = idTrip
        