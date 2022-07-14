from payment import Payment

class Bank(Payment):
    bankname             = str
    identification       = str
    numberAccount        = int
    
    def __init__(self,id, typePayment, ammount, date, bankname, identification, numberAccount):
        super().__init__(id, typePayment, ammount, date)
        self.bankname         = bankname
        self.identification   = identification
        self.numberAccount    = numberAccount