import random

class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)
        for i in range(fim -1):
            posicao_do_minimo = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


    def bolha_melhorada(self, lista):
        fim = len(lista)
        
        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return

class lista_compara:
    
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] # Cria uma lista com n inteiros aleatórios entre 0 e 999
        return lista
    
    def lista_quase_ordenada(self,n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista



