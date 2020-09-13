from namirnice.hrana import Hrana
from random import randint

class Prilog(Hrana):
    def __init__(self, naziv):
        super().__init__(naziv)
        self.cena = randint(20,100)

