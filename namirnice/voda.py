from namirnice.sok import Sok
from random import randint

class Voda(Sok):
    def __init__(self, naziv, zapremina):
        super().__init__(naziv, zapremina)
        self.cena = randint(150,500)