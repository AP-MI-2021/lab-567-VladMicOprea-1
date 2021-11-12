from Domain.carte import getTipReducereClient, creeazaCarte, getID, getTitlu, getGen, getPret


def discount(lista):
    '''
    aplica un discount de 5% pentru toate reducerile silver și de 10% pentru toate reducerile gold.
    :param lista: lista de carti
    :return: lista in care se aplica un discount de 5% pentru toate reducerile silver și de 10% pentru toate reducerile gold.
    '''
    listaNoua = []
    for carte in lista:
        if getTipReducereClient(carte) == "silver":
            carteNoua = creeazaCarte(
                getID(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte) - 5 / 100 * getPret(carte),
                getTipReducereClient(carte)
            )
            listaNoua.append(carteNoua)
        elif getTipReducereClient(carte) == "gold":
            carteNoua = creeazaCarte(
                getID(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte) - 10 / 100 * getPret(carte),
                getTipReducereClient(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def modificareLista(titlu, gen, lista):
    '''
    Modifica genul pentru un titlu dat
    :param titlu: string
    :param lista: lista de carti
    :return: lista in care se modifica genul pentru un titlu dat
    '''
    listaNoua = []
    for carte in lista:
        if getTitlu(carte) == titlu:
            carteNoua = creeazaCarte(
                getID(carte),
                getTitlu(carte),
                gen,
                getPret(carte),
                getTipReducereClient(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def pretMinim(lista):
    '''
    determina pretul minim pentru fiecare gen
    :param lista: lista de carti
    :return: dictionar in care se determina pretul minim pentru fiecare gen
    '''
    minim = {}
    for carte in lista:
        gen = getGen(carte)
        pret = getPret(carte)
        if gen in minim:
            if pret < minim[gen]:
                minim[gen] = pret
        else:
            minim[gen] = pret
    return minim


def pret(carte):
    return getPret(carte)


def ordonareDupaPret(lista):
    '''
    sorteaza cartile dupa pretul lor
    :return: lista sortata de carti dupa pret
    '''
    return sorted(lista, key=pret)

def cartiCuTitluriDistincte(lista):
    '''
    determina numarul de titluri distincte pentru fiecare gen
    :param lista: lista de carti
    :return: numarul de titluri distincte pentru fiecare gen
    '''
    nr = 1
    rezultat = {}
    for carte in lista:
        gen = getGen(carte)
        titlu = getTitlu(carte)
        if gen in rezultat:
            if titlu != rezultat[gen]:
                nr = nr+1
                rezultat[gen] = nr
        else:
            rezultat[gen] = 1
    return rezultat