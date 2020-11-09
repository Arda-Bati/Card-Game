from Player import *

class Game():
    """ This represents a single game between two players. It creates two
    Player instances, deals them a certain number of cards. Then it implements
    each round of the game, calculating an logging the output. Finally, it
    logs the winner(s) of the game."""
    # Class Attributes
    MAX_DECK_SIZE = int(len(full_deck) / 2)
    PLAYERS_COUNT = 2
    suit_tie_breaker = ["SS", "WM", "YE", "DC"]

    # Constructor
    def __init__(self, cards_per_player, player_names):
        """ Consturctor for the Game class. First processes the parameters
        with the process input method. If the result is False, calls
        print("Game not populated") and quits. If result is True initializes
        the instance attributes.

        Requirements: Should call the process_input method of Game with the
        given parameters.

        Instance attributes to initialize:
        deck(full_deck): initialized as a deep copy of full_deck.
            This deck will be shuffled during tests: random.shuffle(self.deck)
        cards_per_player(int): set according to the given parameter
        players(list): First initialized as empty list. It is then populated
            by two player instances, created according to the player_names.

        Parameters:
        cards_per_player(int): How many cards should be dealt to each player
        player_names(list): List of player names (strings)

        Returns: None
        """
        param_ok = Game.process_input(cards_per_player, player_names)
        if param_ok:
            self.deck = list(full_deck)
            self.cards_per_player = cards_per_player
            self.players = []
            for player_name in player_names:
                self.players.append(Player(player_name))
        else:
            print("Game not populated")

    def deal_cards(self):
        """
        Deals cards_per_player (unique) cards to each player in self.players
        Removes these cards from the deck of Game. Each card in the deck is in
        tuple form. According to the type specified in this tuple, this method
        creates a new card.
        ie. ("Warrior 9", "WM")   --> Warrior_Card("Warrior 9")
        ie. ("Dragon 6", "DC")    --> Dragon_Card("Dragon 6")
        ie. ("Secret 2", "SS")    --> Secret_Card("Secret 2")
        ie. ("Emissary 4", "YE")  --> Yuxuan_Card("Emissary 4")

        You should use the __add__method while adding, such as
        self.player += new_card
        """
        for self.player in self.players:
            for i in range(self.cards_per_player):
                card_name, card_type = self.deck.pop(0) #card removed from deck
                if card_type == "WM":
                    new_card = Warrior_Card(card_name)
                elif card_type == "DC":
                    new_card = Dragon_Card(card_name)
                elif card_type == "SS":
                    new_card = Secret_Card(card_name)
                else: # card_type == "YE":
                    new_card = Yuxuan_Card(card_name)
                self.player += new_card

    def play(self):
        """ Plays cards_per_player rounds of the game, until both players run
        of of cards. At each round, it removes the first card of player.cards
        for each player instance. It then compares these cards (using the
        comparators of Card class). It breaks ties according to the index of
        suit_tie_breaker (higher index means winner). It calls log_round
        method during each round and adds to the current log. When the final
        round is over, it calls the log_winners method and adds the result to
        log. Finally, it sets cards_per_player to 0 and returns the log.
        """
        log = ""
        for cur_round in range(self.cards_per_player):
                pla0_card = self.players[0].cards.pop(0)
                pla1_card = self.players[1].cards.pop(0)
                cur_cards = [pla0_card, pla1_card]
                if pla0_card  > pla1_card:
                    winner = 0
                elif pla0_card == pla1_card:
                    pla0_suit = Game.suit_tie_breaker.index(pla0_card.suit)
                    pla1_suit = Game.suit_tie_breaker.index(pla1_card.suit)
                    winner = (pla0_suit < pla1_suit) * 1
                else: # pla1_card < pla2_card:
                    winner = 1
                score_gained = 1 + Card.card_types.index(cur_cards[winner].\
                                                         card_type)
                self.players[winner].score += score_gained
                log += self.log_round(cur_round, winner, \
                            [pla0_card, pla1_card], score_gained)
        log += self.log_winners()
        self.cards_per_player = 0
        return log

    def process_input(cards_per_player, player_names):
        """ Processes the input according to the given Class Attributes.
        Validates the inputs cards_per_player(int) and player_names(list)
        There should be PLAYERS_COUNT players and cards_per_player should be
        <= MAX_DECK_SIZE.

        Requirements: Should have a try catch block validating the input. The
        following should be checked, types of both inputs. player_names' lenght
        is equal to PLAYERS_COUNT. cards_per_player is <= MAX_DECK_SIZE.
        Finally all elements of player_names should have type str

        Parameters:
        cards_per_player(int)
        player_names(list): All elements are strings

        Returns: boolean (True if parameters valid, False otherwise)
        """
        try:
            bool_val = isinstance(player_names, list) and (len(player_names)\
                       == Game.PLAYERS_COUNT) and all(isinstance(elem, str) \
                   for elem in player_names) and isinstance(cards_per_player,\
                       int) and cards_per_player <= Game.MAX_DECK_SIZE
            if bool_val == False:
                raise ValueError()
        except:
            print("Something is wrong with the parameters")
            return False
        return True

    def log_round(self, round_num, winner, cards, score_gained):
        """ Logs round info according to the given parameters, and as shown on
        the write-up and doctests. Appends an empty line at the end.

        Parameters:
        round_num(int): Indicates the current round number - 1
        winner(int): 0 or 1, indicates the index of the winning player
        cards(list): Contains the two cards of the current round. cards[0] is
            the card of players[0]. cards[1] is the card of players[1].
        score_gained(int): indicates the score gained by the winner player.

        Returns: log(str): Log of the current round.
        """
        winner_player = self.players[winner]
        log = ""
        log += "Round: {0}\n".format(round_num + 1)
        log += "Card 1: {0}\n".format(cards[0])
        log += "Card 2: {0}\n".format(cards[1])
        log += "Winner: {0}, total score: {1}\n".format(winner_player.name, \
                                              winner_player.score)
        log += "Score gained by {0}: {1}\n".format(winner_player.name,\
                                          score_gained)
        log += "Winner Card: {0}\n".format(cards[winner].name)
        log += "The card chants: {0}\n".format(cards[winner].chant)
        log += "Player's Total Scores: {0}: {1} points, {2}: {3} points\n\n"\
        .format(self.players[0].name, self.players[0].score,\
                self.players[1].name, self.players[1].score)
        return log

    def log_winners(self):
        """ Logs the winner(s) of the game according to scores. For example:
        If only Player_1 has higher score, so Player_1 won:
        log = Winning player: Player_1
        If both players have the same score, so both won:
        log = Winning players: Player_1 and Player_2

        Returns: log(str): Log of the winners of this game.
        """
        log = ""
        score0 = self.players[0].score
        score1 = self.players[1].score
        if score0 == score1:
            log += "Winning players: {0} and {1}".format(self.players[0].name,\
                  self.players[1].name)
        elif score0 > score1:
            log += "Winning player: {0}".format(self.players[0].name)
        else: # score0 < score1:
            log += "Winning player: {0}".format(self.players[1].name)
        return log
