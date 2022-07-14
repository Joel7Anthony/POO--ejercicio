from payment import Payment
from bank import Bank

class Transfer(Bank):
    
    def __init__(self, id, typePayment, ammount, date, bankname, identification, numberAccount):
        super().__init__(id, typePayment, ammount, date, bankname, identification, numberAccount)