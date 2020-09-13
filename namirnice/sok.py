from namirnica import Namirnica

class Sok(Namirnica):
    def __init__(self, naziv, zapremina):
        super().__init__(naziv)
        self.zapremina = zapremina

    def get_zapremina(self):
        return self.zapremina

    def set_zapremina(self,value):
        self.zapremina = value

