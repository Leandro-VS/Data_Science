def encontra_impares(lista):
    lista_impares = []
    if len(lista) > 0:
        n = lista.pop(0)
        if n % 2 != 0:
            lista_impares.append(n)
        lista_impares = lista_impares + encontra_impares(lista)
    return lista_impares
