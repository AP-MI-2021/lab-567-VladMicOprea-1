from Domain.carte import getID, getTitlu, getGen, getPret, getTipReducereClient
from Logic.CRUD import adaugaCarte, getByID, stergereCarte, modificaCarte


def testAdaugaCarte():
    '''
    verifica daca functia este corecta
    :return: o lista continand vechile carti si noile carti
    '''
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)

    assert getID(getByID("1", lista)) == "1"
    assert getTitlu(getByID("1", lista)) == "Ion"
    assert getGen(lista[0]) == "roman"
    assert getPret(lista[0]) == 50.0
    assert getTipReducereClient(lista[0]) == "silver"

def testStergereCarte():
    '''
    verifica daca functia este corecta
    :return: o noua lista de carti
    '''
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    lista = stergereCarte("1", lista)
    assert len(lista) == 1
    assert getByID("1", lista) is None
    assert getByID("2", lista) is not None

def testModificaCartea():
    '''
    verifica daca functia este corecta
    :return: o lista modificata de carti
    '''
    lista = []
    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)
    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    lista = modificaCarte("2", "Povestea lui Harap-Alb", "basm", 40.0, "gold", lista)

    carteUpdatata = getByID("2", lista)

    assert getID(carteUpdatata) == "2"
    assert getTitlu(carteUpdatata) == "Povestea lui Harap-Alb"
    assert getGen(carteUpdatata) == "basm"
    assert getPret(carteUpdatata) == 40.0
    assert getTipReducereClient(carteUpdatata) == "gold"