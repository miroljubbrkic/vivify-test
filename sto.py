from datetime import datetime

class Sto:
    def __init__(self,rbr):
        self.rbr = rbr
        self.porudzbine = []

    def get_rbr(self):
        return self.rbr

    def set_rbr(self,value):
        self.rbr = value

    def proveri_racun(self):
        for p in self.porudzbine:
            if p.naplaceno == False:
                raise Exception
                break

    def dodaj_porudzbinu(self,porudzbina):
        try:
            self.proveri_racun()
            self.porudzbine.append(porudzbina)
        except Exception:
            print("Nije moguće izdati novu porudžbinu jer prethodna nije plaćena!")
            

    def print_porudzbina(self,rbr_porudzbine=0):
        rbr_porudzbine = len(self.porudzbine)-1
        print("Porudzbina: datum {} sto broj: {}, naplaceno: {}".format(self.porudzbine[rbr_porudzbine].datum, self.rbr,self.porudzbine[rbr_porudzbine].naplaceno))

    def print_racun(self,rbr_porudzbine=0):
        rbr_porudzbine = len(self.porudzbine)-1
        self.porudzbine[rbr_porudzbine].naplaceno = True
        print("Racun: datum {} sto broj {}, naplata {}".format(self.porudzbine[rbr_porudzbine].datum,self.rbr,self.porudzbine[rbr_porudzbine].ukupna_cena))