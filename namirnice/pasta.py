from namirnice.hrana import Hrana
from random import randint

class Pasta(Hrana):
    def __init__(self, naziv):
        super().__init__(naziv)
        self.cena = randint(300,600)