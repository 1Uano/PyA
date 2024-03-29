import cards, games

class BJ_Cards(cards.Positionable_Card):
    """ Карта для игры в Блек - джек. """  
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Cards.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ Колода игральных карт в Блек - джек. """
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS: 
                self.cards.append(BJ_Cards(rank, suit))

class BJ_Hand(cards.Hand):
    """ Рука игрока в Блек - джек. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name


    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        contains_ace = False
        for card in self.cards:
            t+= card.value
            if card.value == BJ_Cards.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Игрок в Блэк-Джек"""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", у вас" + self.player + ", будете брать еще карты")
        return response == "y"
    def bust(self):
        print(self.name, "перебрал(а).")
    def lose(self):
        print(self.name, "проиграл(а).")
    def win(self):
        print(self.name, "выиграл(а).")
    def push(self):
        print(self.name, "сыграл(а) с диллером в ничью.")


class BJ_Dealer(BJ_Hand):
    """ Диллер в Блек - Джек."""
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, "перебрал.")
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game:
    """Игра в Блек - Джек"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Диллер")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()

        for player in self.players:
            print(player)
        print(self.dealer)
        
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                player.win()
            else:
                for player.total in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()
def main():
    print("\t\tДобро пожпловать в Black Jack! \n")

    names = []
    number = games.ask_number("Сколько всего игроков? (1-7): ",
        low = 1, high = 7)
    for i in range(number):
        name = input("Введите имя тгрока № " + str(i + 1) + " :")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть ещё раз")

main()
