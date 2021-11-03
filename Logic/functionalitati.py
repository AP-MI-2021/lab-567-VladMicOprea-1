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
                getPret(carte) - 5/100 * getPret(carte),
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