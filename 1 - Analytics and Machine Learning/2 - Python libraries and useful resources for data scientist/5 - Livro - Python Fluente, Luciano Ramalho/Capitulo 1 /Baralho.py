# Lib que implementa classes especializadas para diversas tarefas
import collections

# namedtuple é usada para criar classes de objetos sem método, apenas com atributos
Card = collections.namedtuple('Card', ['rank', 'suit'])

# Classe Baralho Francês
class FreenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spade diamonds clubs hearts'.split()

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
