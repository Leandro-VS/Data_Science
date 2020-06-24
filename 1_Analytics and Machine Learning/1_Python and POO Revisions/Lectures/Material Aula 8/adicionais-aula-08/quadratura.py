'''
Este módulo provê duas funções para quadratura (integração numérica) usando
o método do trapézio.
'''

def trapezoide_intervalos(f, a, b, n):
    h = (b - a) / n
    s = (f(a) + f(b)) * h / 2
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def trapezoide_precisao(f, a, b, epsilon):
    itercorr, ninterv, h = 0, 1, (b - a)
    s = (f(a) + f(b)) * h / 2
    olds = 0
    while abs(s - olds) >= epsilon or itercorr < 4:
        itercorr, ninterv, h = itercorr + 1, ninterv * 2, h / 2
        if itercorr > 25:
            raise Exception("Falta de convergência em trapezoide_precisao")
        olds = s
        s = 0
        for i in range(1, ninterv, 2):
            s += f(a + i * h)
        s = s * h + olds / 2
    return s

if __name__ == '__main__':
    import math
    print(trapezoide_intervalos(math.sin, 0, 2*math.pi, 1000))
