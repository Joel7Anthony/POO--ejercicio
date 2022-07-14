class Rute():
    start       = []
    end         = []
    KmDistance  = int
    timeAprox   = int
    payAprox    = float
    
    def __init__(self, start, end, KmDistance, timeAprox, payAprox):
        self.start      = start
        self.end        = end
        self.KmDistance = KmDistance 
        self.payAprox   = payAprox
    
    
    