from Domain.carte import toString
from Logic.CRUD import modificaCarte, stergereCarte, adaugaCarte


def uiAdaugaCarte(listaComenzi,lista):
    try:
        ID = input(listaComenzi[1])
        titlu = input(listaComenzi[2])
        gen = input(listaComenzi[3])
        pret = float(input(listaComenzi[4]))
        tipReducereClient = input(listaComenzi[5])
        return adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereCarte(listaComenzi,lista):
    try:
        ID = input(listaComenzi[1])
        return stergereCarte(ID, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaCarte(listaComenzi,lista):
    try:
        ID = input(listaComenzi[1])
        titlu = input(listaComenzi[2])
        gen = input(listaComenzi[3])
        pret = float(input(listaComenzi[4]))
        tipReducereClient = input(listaComenzi[5])
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
    Iesire
     """)

def Menu2(lista):
    try:
        while True:
            Help()
            comenzi = input("Comenzi separate prin ';' si instructiunile comenzii separate prin ','")
            comenzi = comenzi.split(";")
            for comanda in comenzi:
                comanda = comanda.split(",")
            listaComenzi = []
            for detalii in comanda:
                listaComenzi.append(detalii)
                if listaComenzi[0] == "Add" :
                    lista = uiAdaugaCarte(listaComenzi, lista)
                elif listaComenzi[0] == "Delete":
                    lista = uiStergereCarte(listaComenzi, lista)
                elif listaComenzi[0] == "Modify":
                    lista = uiModificaCarte(listaComenzi, lista)
                elif listaComenzi[0] == "Show all":
                    showAll(lista)
                elif listaComenzi[0] == "Iesire":
                    break
                else:
                    print("Optiune gresita! Reincercati: ")
    except Exception as ex:
        print("Eroare, reincercati!", ex)