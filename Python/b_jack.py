import random


class Card:
    def __init__(self, suit, rank, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.card = {}
        self.hidden = None

    def __str__(self):
        if self.hidden is True:
            return '?'
        else:
            return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def hide_card(self):
        self.hidden = True

    def reveal_card(self):
        self.hidden = False



class Deck:
    def __init__(self, numdecks=5):
        self.contents = self.create_deck(numdecks)

    def create_deck(self, numdecks):
        master_list = {
            'hearts': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                       'Q': 10,
                       'K': 10,
                       'A': 1},
            'spades': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                       'Q': 10,
                       'K': 10,
                       'A': 1},
            'diamonds': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                         'Q': 10,
                         'K': 10,
                         'A': 1},
            'clubs': {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                      'Q': 10, 'K': 10,
                      'A': 1}}
        gamedeck = []
        for times in range(numdecks):
            for k, v, in master_list.items():
                for x, y in v.items():
                    gamedeck.append(Card(k, x, y))
        return gamedeck


class Hand:
    def __init__(self, name):
        self.contents = []
        self.name = name
        self.value = self.hand_value()

    def __str__(self):
        return '{} - {}'.format(self.contents, self.value)

    def __repr__(self):
        return '{} of {}'.format(self.contents, self.value)

    def take_card(self, card):
        self.contents.append(card)
        self.hand_value()
        self.score_hand()

    def hand_value(self):
        self.value = 0
        for i in self.contents:
            self.value += i.value

    def score_hand(self):
        self.score = 0
        aces = False
        for i in self.contents:
            if i.value == 1:
                aces = True
                self.score += 1
            else:
                self.score += i.value
        if aces:
            if self.score + 10 <= 21:
                self.score += 10


class DealerHand(Hand):
    def __init__(self):
        Hand.__init__(self)

    def d_hit(self, deck):
        while self.value <= 16:
            self.contents.append(deck.pop())
            self.hand_value()
            continue


class BlackJackGame():
    def __init__(self, player1='player1', player2='player2'):
        self.dealer = DealerHand()
        self.deck = Deck()
        self.player1 = Hand()
        self.player2 = Hand()
        self.players = [self.player1, self.player2, self.dealer]

    def shuffle(self):
        random.shuffle(self.deck.contents)

    def run_game(self):
        busted = False
        self.shuffle()
        for times in range(2):
            self.player1.take_card(self.deck.contents.pop())
            self.player2.take_card(self.deck.contents.pop())
            self.dealer.take_card(self.deck.contents.pop())
        for peeps in self.players:
            print(peeps)
        for peeps in self.players:
            if peeps.value == 20:
                print('Blackjack!')




new_game = BlackJackGame(input('Name of player 1: '), input('Name of player 2: '))
new_game.run_game()
