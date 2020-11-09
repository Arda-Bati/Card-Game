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
        with the process_input method. If the result is False, runs
        print("Game not populated") and quits. If result is True, initializes
        the instance attributes as below:.

        Requirements: Should call the process_input method of Game with the
        given parameters.

        Instance attributes to initialize:
        deck(full_deck): initialized as a deep copy of full_deck.
            This deck will be shuffled during tests: random.shuffle(self.deck)
            (not in this function, but in the doctests)
        cards_per_player(int): set according to the given parameter
        players(list): First initialized as empty list. It is then populated
            by two player instances, created according to the player_names.

        Parameters:
        cards_per_player(int): How many cards should be dealt to each player
        player_names(list): List of player names (strings)

        Returns: None
        """
        ## YOUR CODE IS HERE ##

    def deal_cards(self):
        """
        Deals cards_per_player (unique) cards to each player in self.players
        Removes these cards from the deck of Game. Each card in the deck is in
        tuple form. According to the type specified in this tuple, this method
        creates a new card as below, then adds it to the players' cards.
        ie. ("Warrior 9", "WM")   --> Warrior_Card("Warrior 9")
        ie. ("Dragon 6", "DC")    --> Dragon_Card("Dragon 6")
        ie. ("Secret 2", "SS")    --> Secret_Card("Secret 2")
        ie. ("Emissary 4", "YE")  --> Yuxuan_Card("Emissary 4")

        To deal cards, it gives the first cards_per_player cards in self.deck
        to the first player (removing each card from the deck in the process).
        Then, it gives the remaining first cards_per_player cards to the second
        player.

        You should use the __add__method while adding, such as
        self.player += new_card

        Returns: None
        """
        ## YOUR CODE IS HERE ##

    def play(self):
        """ Plays cards_per_player rounds of the game, until both players run
        out of cards. At each round, it removes the first card of player.cards
        for each player instance. It then compares these cards (using the
        comparators of Card class). It breaks ties according to the index of
        suit_tie_breaker (higher index means winner). It uses log_round
        method during each round and adds to the current log. When the final
        round is over, it uses the log_winners method and adds the result to
        log. Finally, it sets cards_per_player to 0 and returns the log.

        Returns log(str): The complete log of the game, as shown in doctests
        """
        log = ""
        ## YOUR CODE IS HERE ##
        return log

    def process_input(cards_per_player, player_names):
        """ Processes the input according to the given Class Attributes.
        Validates the inputs cards_per_player(int) and player_names(list)
        There should be PLAYERS_COUNT players and cards_per_player should be
        <= MAX_DECK_SIZE.

        Requirements: Should have a try catch block validating the input. The
        following should be checked, types of both inputs. player_names' length
        is equal to PLAYERS_COUNT. cards_per_player is <= MAX_DECK_SIZE.
        Finally all elements of player_names should have type str

        Parameters:
        cards_per_player(int)
        player_names(list): All elements are strings

        Returns: boolean (True if parameters valid, False otherwise)
        """
        ## WRITE YOUR COMMENTS BELOW ##
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
        ## YOUR CODE IS BELOW IN … ##
        ## You can use the \ character if your code exceeds the line limit.
        ## You should uncomment all of the commented code
        log = ""
        # winner_player = self.players[...]
        # log += "Round: {0}\n".format(...)
        # log += "Card 1: {0}\n".format(...)
        # log += "Card 2: {0}\n".format(...)
        # log += "Winner: {0}, total score: {1}\n".format(...)
        # log += "Score gained by {0}: {1}\n".format(...)
        # log += "Winner Card: {0}\n".format(...)
        # log += "The card chants: {0}\n".format(...)
        # log += "Player's Total Scores: {0}: {1} points, {2}: {3} points\n\n"\
        # .format(...)
        return log

    def log_winners(self):
        """ Logs the winner(s) of the game according to scores. For example:
        If only Player_1 has higher score, so Player_1 won:
        log = Winning player: Player_1
        If both players have the same score, so both won:
        log = Winning players: Player_1 and Player_2

        Returns: log(str): Log of the winners of this game.
        """
        ## YOUR CODE IS BELOW IN … ##
        ## You should uncomment all of the commented code
        log = ""
        # score0 = self.players[0].score
        # score1 = self.players[1].score
        # if score0 == score1:
        #     log += "Winning players: {0} and {1}".format(...)
        # elif score0 > score1:
        #     log += "Winning player: {0}".format(...)
        # else: # score0 < score1:
        #     log += "Winning player: {0}".format(...)
        return log
