class Obrok:
    def __init__(self,hrana=[],prilog=[]):
        self.hrana = hrana
        self.prilog = prilog
        self.cena = 0
        
        for h in self.hrana:
            self.cena = self.cena + h.cena

        for p in self.prilog:
            self.cena = self.cena + p.cena