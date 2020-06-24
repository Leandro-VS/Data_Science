import Bhaskara
import pytest

class TestBhaskara():

    @pytest.fixture
    def y(self):
        return Bhaskara.Bhaskara()
    
    def testa_uma_raiz(self, y):
        assert y.calcula_raiz(1,0,0) == (1,0)

    def testa_duas_raizes(self, y):
        assert y.calcula_raiz(1,-5,6) == (2,3,2)

    def testa_zero_raizes(self, y):
        assert y.calcula_raiz(10,10,10) == 0

    def testa_raiz_negativa(self, y):
        assert y.calcula_raiz(10,20,10) == (1,-1)
