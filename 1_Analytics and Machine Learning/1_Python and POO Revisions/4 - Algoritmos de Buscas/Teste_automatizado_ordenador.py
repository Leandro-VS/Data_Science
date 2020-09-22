import Ordenador
import pytest

class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return Ordenador.Ordenador()
    
    @pytest.fixture
    def l_quase(self):
        l_quase = Ordenador.lista_compara()
        return l_quase.lista_quase_ordenada(100)
    
    @pytest.fixture
    def l_aleat(self):
        l_aleatoria = Ordenador.lista_compara()
        return l_aleatoria.lista_aleatoria(100)
    
    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
            else:
                return True
    
    def test_bolha_melhorada_aleatoria(self, o,  l_aleat):
        o.bolha_melhorada(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_aleatoria(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bolha_melhorada_quase(self, o,  l_quase):
        o.bolha_melhorada(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)
