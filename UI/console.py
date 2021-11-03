from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergereCarte, modificaCarte
from Logic.functionalitati import discount, modificareLista


def printMenu():
    print("1. Adauga carte")
    print("2. Sterge carte")
    print("3. Modifica carte")
    print("4. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold")
    print("5. Modificarea genului pentru un titlu dat")
    print("a. Afisare carti")
    print("0. Iesire")


def uiAdaugaCarte(lista):
    try:
        ID = input("Dati ID-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input("Dati pretul: "))
        tipReducereClient = input("Dati tipul reducerii clientului: ")
        return adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereCarte(lista):
    try:
        ID = input("Dati noul ID: ")
        return stergereCarte(ID, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaCarte(lista):
    try:
        ID = input("Dati ID-ul: ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati noul gen: ")
        pret = float(input("Dati noul pret: "))
        tipReducereClient = input("Dati noul tip de reducere al clientului: ")
        return modificaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for carte in lista:
        print(toString(carte))


def uiDiscount(lista):
    return discount(lista)

def uiModificareLista(lista):
    titlu = input("Dati noul titlu: ")
    gen = input("Dati noul gen: ")
    return modificareLista(titlu, gen, lista)

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCarte(lista)
        elif optiune == "2":
            lista = uiStergereCarte(lista)
        elif optiune == "3":
            lista = uiModificaCarte(lista)
        elif optiune == "4":
            lista = uiDiscount(lista)
        elif optiune == "5":
            lista = uiModificareLista(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "0":
            break
        else:
            print("Optiune gresita! Reincercati: ")
