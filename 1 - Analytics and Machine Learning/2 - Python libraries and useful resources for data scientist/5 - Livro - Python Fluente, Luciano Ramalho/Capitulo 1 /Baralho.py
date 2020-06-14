# Lib que implementa classes especializadas para diversas tarefas
import collections

"""
Métodos especiais do python são métodos implementados na linguagem, sempre no seguinte padrão:__método__
são úteis em diversas situações e nos permitem usa-los para tarefas simples
"""

# namedtuple é usada para criar classes de objetos sem método, apenas com atributos
Card = collections.namedtuple('Card', ['rank', 'suit'])

# Classe Baralho Francês
class FreenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(ranks, suit) for suit in self.suits
                                        for ranks in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FreenchDeck()
print(len(deck))
print("----------------------------------")
print()

print(deck[0])
print(deck[-1])
print("----------------------------------")
print()

#Não precisamos criar um método para escolher valores aleatórios numa lista, podemos usar
#uma função propria do python
from random import choice

print("Escolhas aleatórias do baralho")
print(choice(deck))
print(choice(deck))
print(choice(deck))
print("----------------------------------")
print()

#Ao utilizar o método especial __getitem__ herdamos naturalmente a propriedades de utilizar o slice,
#assim como iterar sobre objetos

print("SLICE")
print(deck[:3])
print(deck[12::13])
print()
print("Iterável")
for card in deck[:5]:
    print(card)
print()
print("Iteração reversa")
for card in reversed(deck[-5:]):
    print(card)
print("----------------------------------")
print()

#Ranqueando as cartas do baralho
#Como a classe contém o método especial __getitem__ ela se torna 'iterável'
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

print("Rankeando e ordenando o baralho")
#Função que atribui um rank
def spades_high(card):
    rank_value = FreenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

#Lista o baralho em ordem crescente
for card in sorted(deck, key=spades_high):
    print(card)
print("----------------------------------")
print()



