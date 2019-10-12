import random
class Card:
    """ Одна игральная карта. """
    RANKS = ["Т", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "В", "Д", "K"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666'] # ♠ ♣ ♥ ♦
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """ Карта, номинал и масть которой не могут быть выведены на экран. """
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх. """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand:
    """ Рука: набор карт на руках у одного игрока. """
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)




card1 = Card(rank = "Т", suit = Card.SUITS[0])
print("Вывожу на экран объект-карту:")
print(card1)
class Deck(Hand):
    """ Колода игральных карт. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать: карты закончились!")
                    

rank = ["Т", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "В", "Д", "K"]
card2 = Card(rank = str(rank[random.randint(0,12)]), suit = Card.SUITS[0])
card3 = Card(rank = str(rank[random.randint(0,12)]), suit = Card.SUITS[0])
card4 = Card(rank = str(rank[random.randint(0,12)]), suit = Card.SUITS[0])
card5 = Card(rank = str(rank[random.randint(0,12)]), suit = Card.SUITS[0])
print("\nВывожу еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)


my_hand = Hand()
print("\nПечатаю карты, которые у меня на руках до раздачи:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю пять карт, которые появились у меня на руках:")
print(my_hand)



your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПервые две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("А у меня на руках:")
print(my_hand)



my_hand.clear()
print("\nА у меня на руках после того, как я сбросил все карты:")
print(my_hand)



deck1 = Deck()
print("Создана новая колода.")
print("Вот эта колода:")
print(deck1)
deck1.populate()
print("\nВ колоде появились карты.")
print("Вот как она выглядит теперь:")
deck1.shuffle()
print(deck1)


my_hand = Hand()
your_hand = Hand()
his_hand = Hand()
hands = [my_hand, your_hand, his_hand]
deck1.deal(hands, per_hand = 2)
print("\nМне и вам на руки роздано по 5 карт.")
print("У меня на руках:")
print(my_hand)
print("У вас на руках:")
print(your_hand)
print("У него на руках:")
print(his_hand)
print("Осталось в колоде:")
print(deck1)

card1 = Card("Т", Card.SUITS[0])
card2 = Unprintable_Card("Т", Card.SUITS[1])
card3 = Positionable_Card("Т", Card.SUITS[2])

print("Печатаю объект Card:")
print(card1)

print("\nПечатаю объект Unprintable_Card:")
print(card2)

print("\nПечатаю объект Positionable_Card:")
print(card3)
print("Пероворачиваю объект Positionable_Card.")
card3.flip()
print("Печатаю объект Positionable_Card:")
print(card3)

if __name