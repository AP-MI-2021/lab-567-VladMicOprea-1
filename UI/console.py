from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergereCarte, modificaCarte


def printMenu():
    print("1. Adauga carte")
    print("2. Sterge carte")
    print("3. Modifica carte")
    print("a. Afisare carti")
    print("0. Iesire")

def uiAdaugaCarte(lista):
    ID = input("Dati ID-ul: ")
    titlu = input("Dati titlul: ")
    gen = input("Dati genul: ")
    pret = float(input("Dati pretul: "))
    tipReducereClient = input("Dati tipul reducerii clientului: ")
    return adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista)

def uiStergereCarte(lista):
    ID = input("Dati noul ID: ")
    return stergereCarte(ID, lista)

def uiModificaCarte(lista):
    ID = input("Dati ID-ul: ")
    titlu = input("Dati noul titlu: ")
    gen = input("Dati noul gen: ")
    pret = float(input("Dati noul pret: "))
    tipReducereClient = input("Dati noul tip de reducere al clientului: ")
    return modificaCarte(ID, titlu, gen, pret, tipReducereClient, lista)

def showAll(lista):
    for carte in lista:
        print(toString(carte))

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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "0":
            break
        else:
            print("Optiune gresita! Reincercati: ")