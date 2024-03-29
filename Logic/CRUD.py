from Domain.carte import creeazaCarte, getID, getTipReducereClient, getPret


def adaugaCarte(ID, titlu, gen, pret, tipReducereClient, lista):
    '''
    adauga o carte intr-o lista
    :param ID: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tipReducereClient: string
    :param lista: lista de carti
    :return: o lista continand vechile carti si noile carti
    '''
    if getByID(id, lista) is not None:
        raise ValueError(":ID-ul este deja folosit")
    carte = creeazaCarte(ID, titlu, gen, pret, tipReducereClient)
    if getPret(carte) < 0:
        raise ValueError(":pretul este negativ! Incorect")
    if getTipReducereClient(carte) != "gold" and getTipReducereClient(carte) != "silver":
        raise ValueError(":reducerea adaugata nu exista")
    return lista + [carte]

def getByID(ID, lista):
    '''
    da elementul din lista cu un ID dat
    :param ID: string
    :param lista: lista de carti
    :return: cartea cu ID-ul dat sau None daca nu exsista
    '''
    for carte in lista:
        if getID(carte) == ID:
            return carte

def stergereCarte(ID, lista):
    '''
    sterge o carte cu ID-ul dat din lista
    :param ID: string
    :param lista: lista de carti
    :return: o lista de carti fara elementul cu ID-ul dat
    '''
    return [carte for carte in lista if getID(carte) != ID]

def modificaCarte(ID, titlu, gen, pret, tipReducereClient, lista):
    '''
    modifica o carte cu ID-ul dat
    :param ID: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tipReducereClient: string
    :param lista: lista de carti
    :return: o lista modificata de carti
    '''
    listaNoua = []
    for carte in lista:
        if getID(carte) == ID:
            carteNoua = creeazaCarte(ID, titlu, gen, pret, tipReducereClient)
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua