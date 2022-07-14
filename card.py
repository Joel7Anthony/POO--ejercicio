from bank import Bank

class Card(Bank):
    cardNumber          = int
    cardSecurityCode    = int
    cardDate            = int
    
    def __init__(self, id, ammount, typePayment, date, bankname, identification, numberAccount, cardNumber, carDate, cardSecurityCode):
        super().__init__(id, ammount, typePayment, date, bankname, identification, numberAccount)
        self.cardDate          = carDate
        self.cardNumber        = cardNumber
        self.cardSecurityCode  = cardSecurityCode