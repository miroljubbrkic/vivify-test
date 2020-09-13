from namirnice.pasta import Pasta
from namirnice.pizza import Pizza
from namirnice.prilog import Prilog
from namirnice.hrana import Hrana

from namirnice.gazirani import Gazirani
from namirnice.negazirani import Negazirani
from namirnice.voda import Voda
from namirnice.sok import Sok

from obrok import Obrok
from porudzbina import Porudzbina
from sto import Sto

from datetime import datetime

sto1 = Sto("1")
sto2 = Sto("2")
sto3 = Sto("3")
sto4 = Sto("4")

pizza_capricciosa = Pizza("pizza capricciosa")
pizza_siciliana = Pizza("pizza_siciliana")
pizza3 = Pizza("Pizza3")
pizza4 = Pizza("Pizza4")

pasta_italijana = Pasta("Pasta italijana")
pasta_carbonara = Pasta("pasta carbonara")
pasta3 = Pasta("Pasta3")
pasta4 = Pasta("Pasta4")
pasta5 = Pasta("Pasta5")

gazirani_sok = Gazirani("gazirani sok",0.5)
negazirani_sok = Negazirani("negazirani sok",0.25)
voda = Voda("voda",1000)

kecap = Prilog("kecap")
origano = Prilog("origano")
extra_cheese = Prilog("extra cheese")
prilog4 = Prilog("Prilog4")
prilog5 = Prilog("Prilog5")

#? ==========================================


o1 = Obrok([pizza_capricciosa],[kecap,origano])
p1 = Porudzbina(o1,[gazirani_sok,gazirani_sok])
sto1.dodaj_porudzbinu(p1)
sto1.print_porudzbina()
sto1.print_racun()
sto1.print_porudzbina()

print("###############################################")

o2 = Obrok([pizza_siciliana,pasta_carbonara])
p2 = Porudzbina(o2,[negazirani_sok])
sto2.dodaj_porudzbinu(p2)
sto2.print_porudzbina()
sto2.print_racun()
sto2.print_porudzbina()
sto2.dodaj_porudzbinu(Porudzbina(Obrok([pizza_capricciosa]),[]))
sto2.print_porudzbina()
sto2.dodaj_porudzbinu(Porudzbina(Obrok([pizza_capricciosa]),[]))

print("###############################################")

o3 = Obrok([pizza_capricciosa,pizza_capricciosa,pizza_capricciosa],[kecap,kecap])
p3 = Porudzbina(o3,[gazirani_sok,negazirani_sok,voda])
sto3.dodaj_porudzbinu(p3)
sto3.print_porudzbina()
sto3.print_racun()
sto3.print_porudzbina()
