import math

class Bhaskara():
    def delta(self, a,b,c):
        return b**2 - 4*a*c

    def calcula_raiz(self, a, b, c):
        d = self.delta(a, b, c)
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
    def main(self):
        a_digitado = float(input("Digite o valor de a: "))
        b_digitado = float(input("Digite o valor de b: "))
        c_digitado = float(input("Digite o valor de c: "))
    
        print(self.calcula_raiz(a_digitado, b_digitado, c_digitado))
