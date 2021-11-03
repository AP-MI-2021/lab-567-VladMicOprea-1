from Domain.carte import getPret, getGen
from Logic.CRUD import adaugaCarte, getByID
from Logic.functionalitati import discount, modificareLista


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
