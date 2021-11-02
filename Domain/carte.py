def creeazaCarte(ID, titlu, gen, pret, tipReducereClient):
    '''
    creeaza un dictionar ce reprezinta o carte
    :param ID: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tipReducereClient: string
    :return: un dictionar ce reprezinta o carte
    '''
    return {
        "ID": ID,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "tipReducereClient": tipReducereClient
    }

def getID(carte):
    '''
    da ID-ul unei carti
    :param carte: dictionar ce contine o carte
    :return: ID-ul cartii
    '''
    return carte["ID"]

def getTitlu(carte):
    '''
    da titlul unei carti
    :param carte: dictionar ce contine o carte
    :return: titlul cartii
    '''
    return carte["titlu"]

def getGen(carte):
    '''
    da genul unei cartii
    :param carte: dictionar ce contine o carte
    :return: genul cartii
    '''
    return carte["gen"]

def getPret(carte):
    '''
    da pretul unei carti
    :param carte: dictionar ce contine o carte
    :return: pretul cartii
    '''
    return carte["pret"]

def getTipReducereClient(carte):
    '''
    da tipul reducerii clentului unei carti
    :param carte: dictionar ce contine o carte
    :return: tipul reducerii clientului cartii
    '''
    return carte["tipReducereClient"]

def toString(carte):
    return "ID: {}, titlu: {}, gen: {}, pret: {}, tipReducereClient: {}".format(
        getID(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getTipReducereClient(carte)
    )