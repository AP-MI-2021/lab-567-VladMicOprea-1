from Domain.carte import toString
from Logic.CRUD import modificaCarte, stergereCarte, adaugaCarte


def uiAdaugaCarte(listaComenzi, lista):
    try:
        ID = listaComenzi[0]
        titlu = listaComenzi[1]
        gen = listaComenzi[2]
        pret = float(listaComenzi[3])
        tipReducereClient = listaComenzi[4]
        return adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereCarte(listaComenzi, lista):
    try:
        ID = listaComenzi[0]
        return stergereCarte(ID, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaCarte(listaComenzi, lista):
    try:
        ID = listaComenzi[0]
        titlu = listaComenzi[1]
        gen = listaComenzi[2]
        pret = float(listaComenzi[3])
        tipReducereClient = listaComenzi[4]
        return modificaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def Help():
    '''
    e un nou meniu prin care comenzile sunt separate prin ';' si detaliile prin ','
    :return:
    '''
    print("""
    Add,ID,titlu,gen,pret,tipReducereClient
    Delete,ID
    Modify,ID,titlu,gen,pret,tipReducereClient
    Show all
    help
    Iesire
     """)


def Menu2(lista):
    try:
        while True:
            comenzi = input("Comenzi separate prin ';' si instructiunile comenzii separate prin ','")
            listaComenzi = []
            listaComenzi = comenzi.split(";")
            for comanda in listaComenzi:
                operatie = []
                operatie = comanda.split(",")
                if operatie[0] == "Add":
                    operatie.pop(0)
                    lista = uiAdaugaCarte(operatie, lista)
                elif operatie[0] == "Delete":
                    operatie.pop(0)
                    lista = uiStergereCarte(operatie, lista)
                elif operatie[0] == "Modify":
                    operatie.pop(0)
                    lista = uiModificaCarte(operatie, lista)
                elif operatie[0] == "Show all":
                    showAll(lista)
                elif operatie[0] == "help":
                    Help()
                elif operatie[0] == "Iesire":
                    break
                else:
                    print("Optiune gresita! Reincercati: ")
    except Exception as ex:
        print("Eroare, reincercati!", ex)
