from Logic.CRUD import adaugaCarte


def testUndoRedo():
    lista = []
    undoList = []
    redoList = []
    message = ""

    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)

    undoList.append(lista)
    redoList.clear()

    assert lista == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    lista = adaugaCarte("3", "Moara cu noroc", "nuvela", 40.0, "gold", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'},
                       {'ID': '3', 'titlu': 'Moara cu noroc', 'gen': 'nuvela', 'pret': 40.0,
                        'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        lista = undoList.__getitem__(len(undoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        lista = undoList.__getitem__(len(undoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        if undoList:
            lista = undoList.__getitem__(len(undoList) - 1)
        else:
            lista = []

    assert (lista) == []

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        if undoList:
            lista = undoList.__getitem__(len(undoList) - 1)
        else:
            lista = []

    assert lista == []

    lista = adaugaCarte("1", "Ion", "roman", 50.0, "silver", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    lista = adaugaCarte("2", "Baltagul", "roman", 45.0, "gold", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    lista = adaugaCarte("3", "Moara cu noroc", "nuvela", 40.0, "gold", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'},
                       {'ID': '3', 'titlu': 'Moara cu noroc', 'gen': 'nuvela', 'pret': 40.0,
                        'tipReducereClient': 'gold'}]

    if len(redoList) > 0:
        undoList.append(lista)
        redoList.pop()
        lista = redoList.__getitem__(len(redoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'},
                       {'ID': '3', 'titlu': 'Moara cu noroc', 'gen': 'nuvela', 'pret': 40.0,
                        'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        lista = undoList.__getitem__(len(undoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        lista = undoList.__getitem__(len(undoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                        {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'},
                        {'ID': '3', 'titlu': 'Moara cu noroc', 'gen': 'nuvela', 'pret': 40.0,
                         'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.__getitem__(len(undoList) - 1)
        undoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '2', 'titlu': 'Baltagul', 'gen': 'roman', 'pret': 45.0, 'tipReducereClient': 'gold'}]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.__getitem__(len(undoList) - 1)
        undoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    lista = adaugaCarte("4", "Enigma Otiliei", "roman", 35.0, "silver", lista)

    undoList.append(lista)
    redoList.clear()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '4', 'titlu': 'Enigma Otiliei', 'gen': 'roman', 'pret': 35.0, 'tipReducereClient': 'silver'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '4', 'titlu': 'Enigma Otiliei', 'gen': 'roman', 'pret': 35.0, 'tipReducereClient': 'silver'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        lista = undoList.__getitem__(len(undoList) - 1)

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    if len(undoList) > 0:
        redoList.append(lista)
        undoList.pop()
        if undoList:
            lista = undoList.__getitem__(len(undoList) - 1)
        else:
            lista = []

    assert (lista) == []

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '4', 'titlu': 'Enigma Otiliei', 'gen': 'roman', 'pret': 35.0, 'tipReducereClient': 'silver'}]

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.__getitem__(len(redoList) - 1)
        redoList.pop()

    assert (lista) == [{'ID': '1', 'titlu': 'Ion', 'gen': 'roman', 'pret': 50.0, 'tipReducereClient': 'silver'},
                       {'ID': '4', 'titlu': 'Enigma Otiliei', 'gen': 'roman', 'pret': 35.0, 'tipReducereClient': 'silver'}]
