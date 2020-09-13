from datetime import datetime

class Porudzbina:
    def __init__(self,obrok,sokovi):
        self.obrok = obrok
        self.sokovi = sokovi
        self.naplaceno = False
        self.datum = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.ukupna_cena = self.obrok.cena
        
        for s in self.sokovi:
            self.ukupna_cena = self.ukupna_cena + s.cena

            
        



