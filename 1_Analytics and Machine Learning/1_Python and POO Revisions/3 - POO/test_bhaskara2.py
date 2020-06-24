import math
import pytest

def delta(a,b,c):
    return b**2 - 4*a*c

def calcula_raiz(a, b, c):
        d = delta(a, b, c)
        if d == 0:
            raiz_1 = (-b + math.sqrt(d)) / (2*a)
            return 1,raiz_1
        else:
            if d < 0:
                return 0
            else:
                raiz_1 = (-b + math.sqrt(d)) / (2*a)
                raiz_2 = (-b - math.sqrt(d)) / (2*a)
                return 2, raiz_1, raiz_2


@pytest.mark.parametrize("entrada, esperado", [
    ((1,0,0),(1,0)),
    ((1,-5,6),(2,3,2)),
    ((10,10,10),(0)),
    ((10,20,10),(1,-1)),
    ])
    
def test(entrada, esperado):
	a, b, c = entrada
	assert calcula_raiz(a, b, c) == esperado
