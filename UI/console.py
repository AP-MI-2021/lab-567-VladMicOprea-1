from Domain.carte import toString
from Logic.CRUD import adaugaCarte, stergereCarte, modificaCarte
from Logic.functionalitati import discount, modificareLista, pretMinim, ordonareDupaPret


def printMenu():
    print("1. Adauga carte")
    print("2. Sterge carte")
    print("3. Modifica carte")
    print("4. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7. Ordonarea vanzarilor crescator după pret")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare carti")
    print("0. Iesire")


def uiAdaugaCarte(lista, undoList, redoList):
    try:
        ID = input("Dati ID-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input("Dati pretul: "))
        tipReducereClient = input("Dati tipul reducerii clientului: ")
        rezultat = adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereCarte(lista, undoList, redoList):
    try:
        ID = input("Dati noul ID: ")
        rezultat = stergereCarte(ID, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaCarte(lista, undoList, redoList):
    try:
        ID = input("Dati ID-ul: ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati noul gen: ")
        pret = float(input("Dati noul pret: "))
        tipReducereClient = input("Dati noul tip de reducere al clientului: ")
        rezultat = modificaCarte(ID, titlu, gen, pret, tipReducereClient, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def uiDiscount(lista):
    return discount(lista)


def uiModificareLista(lista, undoList, redoList):
    titlu = input("Dati noul titlu: ")
    gen = input("Dati noul gen: ")
    rezultat = modificareLista(titlu, gen, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat

def uiPretMinim(lista):
    minim = pretMinim(lista)
    for gen in minim:
        print("Genul {} are pretul minim de {}".format(gen, minim[gen]))


def uiOrdonareDupaPret(lista):
    showAll(ordonareDupaPret(lista))


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaCarte(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereCarte(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaCarte(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiDiscount(lista)
        elif optiune == "5":
            lista = uiModificareLista(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMinim(lista)
        elif optiune == "7":
            uiOrdonareDupaPret(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "0":
            break
        else:
            print("Optiune gresita! Reincercati: ")
