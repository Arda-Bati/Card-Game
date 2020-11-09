"""
HW 9, Q4. Tutor Fighter Card Game implementation.
"""

from Game import *
import random

def doctests_go_here():
    """
    Contains all the doctests for the question.

    >>> card = full_deck[12]
    >>> print(card)
    ('Marina the Marvel 50', 'WM')

    # Card Class tests

    >>> card_name1 = full_deck[5][0]
    >>> card_name2 = full_deck[24][0]
    >>> card_name3 = full_deck[37][0]
    >>> card_name4 = full_deck[48][0]
    >>> warrior_card = Warrior_Card(card_name1)
    >>> dragon_card  = Dragon_Card(card_name2)
    >>> secret_card  = Secret_Card(card_name3)
    >>> yuxuan_card  = Yuxuan_Card(card_name4)

    >>> print(warrior_card)
    Card name: Warrior 7, number: 7, suit: WM, card type: ordinary
    >>> print(dragon_card)
    Card name: Nabi the Noble 40, number: 40, suit: DC, card type: special
    >>> print(secret_card)
    Card name: Wesley the Wrecker -20, number: -20, suit: SS, card type: \
special
    >>> print(yuxuan_card)
    Card name: Emissary 11, number: 11, suit: YE, card type: special

    >>> warrior_card.get_skill(dragon_card)
    12
    >>> dragon_card.get_skill(warrior_card)
    0
    >>> secret_card.get_skill(yuxuan_card)
    32
    >>> yuxuan_card.get_skill(dragon_card)
    34

    # Player Class Tests

    >>> Player_1 = Player("Player_1")
    >>> Player_1 + 1
    Incorrect type: got: <class 'int'>, expected Card object, card not added
    Player("Player_1", 0)
    >>> Player_1 + warrior_card + dragon_card
    Player("Player_1", 0)
    >>> for card in Player_1.cards: print(card)
    Card name: Warrior 7, number: 7, suit: WM, card type: ordinary
    Card name: Nabi the Noble 40, number: 40, suit: DC, card type: special
    >>> print(Player_1)
    name: Player_1, score: 0, cards: [Warrior_Card("Warrior 7"), \
Dragon_Card("Nabi the Noble 40")]
    >>> Player_1 = Player_1 - warrior_card - dragon_card
    >>> print(Player_1)
    name: Player_1, score: 0, cards: []
    >>> Player_1 = Player_1 + 3
    Incorrect type: got: <class 'int'>, expected Card object, card not added
    >>> Player_1 = Player_1 + Player_1
    Incorrect type: got: <class 'Player.Player'>, expected Card object\
, card not added

    # Game Class Tests

    # No shuffling for game 0, game gives the first two cards (Warrior 2 and 3)
    # to Player 1, the next two cards (Warrior 4 and 5) to Player 2
    >>> game0 = Game(2, ["Player 1", "Player 2"])
    >>> print(game0.deck[:4])
    [('Warrior 2', 'WM'), ('Warrior 3', 'WM'), ('Warrior 4', 'WM'), \
('Warrior 5', 'WM')]
    >>> game0.deal_cards()
    >>> result = game0.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Warrior 2, number: 2, suit: WM, card type: ordinary
    Card 2: Card name: Warrior 4, number: 4, suit: WM, card type: ordinary
    Winner: Player 2, total score: 1
    Score gained by Player 2: 1
    Winner Card: Warrior 4
    The card chants: Marina before all!
    Player's Total Scores: Player 1: 0 points, Player 2: 1 points
    <BLANKLINE>
    Round: 2
    Card 1: Card name: Warrior 3, number: 3, suit: WM, card type: ordinary
    Card 2: Card name: Warrior 5, number: 5, suit: WM, card type: ordinary
    Winner: Player 2, total score: 2
    Score gained by Player 2: 1
    Winner Card: Warrior 5
    The card chants: Marina before all!
    Player's Total Scores: Player 1: 0 points, Player 2: 2 points
    <BLANKLINE>
    Winning player: Player 2

    >>> game1 = Game(28, ["Player 1", "Player 2"])
    Something is wrong with the parameters
    Game not populated
    >>> game1 = Game(28, [32, "Player 2"])
    Something is wrong with the parameters
    Game not populated
    >>> game1 = Game(1, ["Player_1", "Player_2"])
    >>> random.seed(1)
    >>> random.shuffle(game1.deck)
    >>> print(game1.deck[:2])
    [('Emissary 12', 'YE'), ('Sudi the Sincere 11', 'WM')]
    >>> game1.deal_cards()
    >>> result = game1.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Emissary 12, number: 12, suit: YE, card type: special
    Card 2: Card name: Sudi the Sincere 11, number: 11, suit: WM, card type: \
special
    Winner: Player_1, total score: 2
    Score gained by Player_1: 2
    Winner Card: Emissary 12
    The card chants: I am the Piazza!
    Player's Total Scores: Player_1: 2 points, Player_2: 0 points
    <BLANKLINE>
    Winning player: Player_1

    >>> game2 = Game(2, ["Player_1", "Player_2"])
    >>> random.seed(2)
    >>> random.shuffle(game2.deck)
    >>> print(game2.deck[:4])
    [('Dragon 4', 'DC'), ('Secret 5', 'SS'), ('Sudi the Sincere 11', 'WM'), \
('Dragon 10', 'DC')]
    >>> game2.deal_cards()
    >>> result = game2.play()
    >>> print(result)
    Round: 1
    Card 1: Card name: Dragon 4, number: 4, suit: DC, card type: ordinary
    Card 2: Card name: Sudi the Sincere 11, number: 11, suit: WM, card type: \
special
    Winner: Player_2, total score: 2
    Score gained by Player_2: 2
    Winner Card: Sudi the Sincere 11
    The card chants: Marina before all!
    Player's Total Scores: Player_1: 0 points, Player_2: 2 points
    <BLANKLINE>
    Round: 2
    Card 1: Card name: Secret 5, number: 5, suit: SS, card type: ordinary
    Card 2: Card name: Dragon 10, number: 10, suit: DC, card type: ordinary
    Winner: Player_2, total score: 3
    Score gained by Player_2: 1
    Winner Card: Dragon 10
    The card chants: All hail the Recursive Dragon!
    Player's Total Scores: Player_1: 0 points, Player_2: 3 points
    <BLANKLINE>
    Winning player: Player_2

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    pass
