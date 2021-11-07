from Domain.carte import getPret, getGen, getID
from Logic.CRUD import adaugaCarte, getByID
from Logic.functionalitati import discount, modificareLista, pretMinim, ordonareDupaPret


def testDiscount():
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    lista = discount(lista)

    assert getPret(getByID("1", lista)) == 47.5
    assert getPret(getByID("2", lista)) == 40.5


def testModificareLista():
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "nuvela", 45.0, "gold", lista)

    lista = modificareLista("Baltagul", "roman", lista)
    lista = modificareLista("Ion", "nuvela", lista)

    assert getGen(getByID("2", lista)) == "roman"
    assert getGen(getByID("1", lista)) == "nuvela"

def testPretMinim():
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)
    lista = adaugaCarte("3", "O scrisoare pierduta", "comedie", 30.0, "gold", lista)

    minim = pretMinim(lista)

    assert len(minim) == 2
    assert minim["roman"] == 45.0
    assert minim["comedie"] == 30.0



def testOrdonareDupaPret():
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    rezultat = ordonareDupaPret(lista)

    assert getID(rezultat[0]) == "2"
    assert getID(rezultat[1]) == "1"
