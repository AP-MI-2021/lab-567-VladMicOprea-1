from Domain.carte import creeazaCarte, getID, getTitlu, getGen, getPret, getTipReducereClient


def testCarte():
    '''
    verifica daca functia este corecta
    :return: un dictionar ce reprezinta o carte
    '''
    carte = creeazaCarte("1", "Ion", "roman", 50.0, "silver")
    assert getID(carte) == "1"
    assert getTitlu(carte) == "Ion"
    assert getGen(carte) == "roman"
    assert getPret(carte) == 50.0
    assert getTipReducereClient(carte) == "silver"
