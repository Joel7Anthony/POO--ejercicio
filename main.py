from pprint import pprint
from account import Account
from car import Car
from cash import Cash
from uberConfort import UberConfort
from uberX import UberX


if __name__ == "__main__":
      
   car = Car("PB077777", Account("Anthony Molina", "1722712062", "19") )
   
   print(vars(car))
   print(vars(car.driver))
   
   
   uberX = UberX("PCC-79017", Account("DjMaRIIo","555555"), "Fiat", "Rapt")
   print(vars(uberX))
   print(vars(car.driver))
   
   
   uberConfort = UberConfort("PJK-7545", Account("VEGETTA", "69446654"), "Dodge", "Cuero", "6")
   print(vars(uberConfort))
   print(vars(uberConfort.driver))
   
   padoDinero = Cash("2", "5-7-2022", "20", "Cash")
   print(vars(padoDinero))
   