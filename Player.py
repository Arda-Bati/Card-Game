from Suits import *

class Player():
    """ This class represents one of the two players of the game."""

    # Constructor
    def __init__(self, player_name):
        """ Consturctor for the Player class. Initiazlies a player instance

        Instance attributes to initialize:
        name(str): Player's name (ie. "Player_1")
        cards(list): Should be initialized as an empty list.
        score(int): Should be initialized to 0.

        Parameters:
        player_name (str): The name of the player. Assume it will be a string.

        Returns: None
        """
        self.name = player_name
        self.cards = []
        self.score = 0

    # Add card special method
    def __add__(self, new_card):
        """ Special __add__ method used to add new_card to the player's hand.
        Requirements: call the method process_card to make sure the supplied
        parameter is of correct type. If True add card to the players cards.
        If False, do not operate on the users cards.

        Parameters: new_card(child of Card) a card belonging to one of the 4
        suits. This card should be added to this player's cards.

        Returns self (regardless of input correctness). This way we can write
        operations like:
        player1 + card1 + card2 + card3   # Which proceeds as follows:
        (player1 + card1) + card2 + card3 # the expression in () is executed
                                          # and returns the player1 instance
        (player1 + card2) + card3         # same as above
        (player1 + card3)                 # same as above
        player1                           # the line above returns the instance
        player1.cards --> [card1, card2, card3] # all cards added

        This idea will also be mentioned in the mini discussion.
        """
        card_ok = Player.process_card(new_card)
        if card_ok:
            self.cards.append(new_card)
            return self
        else:
            return self

    # Remove Card special method
    def __sub__(self, old_card):
        """ Special __sub__ method used to remove old_card from the player's
        hand.
        Requirements: call the method process_card to make sure the supplied
        parameter is of correct type. If True remove card from cards list.
        If False, do not operate on cards list.

        Parameters: old_card(child of Card) a card belonging to one of the 4
        suits. This card should be removed from this players cards.

        Returns self (regardless of input correctness): The same idea as add:

        player1.cards --> [card1, card2, card3]
        player1 - card1 - card2 - card3   # Will proceed as follows:
        (player1 - card1) - card2 - card3 # the expression in () is executed
                                          # and returns the player1 instance
        (player1 - card2) - card3         # same as above
        (player1 - card3)                 # same as above
        player1                           # the line above returns the instance
        player1.cards --> []              # all cards removed
        """
        card_ok = Player.process_card(old_card)
        if card_ok:
            self.cards.remove(old_card)
            return self
        else:
            return self

    # String and repr representations
    def __str__(self):
        """ String representation for a Player instance. """
        str_form = "name: {0}, score: {1}, cards: {2}"
        str_form = str_form.format(self.name, self.score, self.cards)
        return str_form
    def __repr__(self):
        """ Repr for a Player instance. """
        repr_form = "{0}(\"{1}\", {2})"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name, self.score)
        return repr_form

    # Helper method
    def process_card(a_card):
        """ Helper method which checks if the supplied card parameter is
        an instance of the Card class. Uses a try - except block.

        Requirements: You should use a try - except block. In the try block
        you should check if isinstance(a_card, Card) (subclasses count as
        instances of the parent class). If false, print the output as shown in
        the doctest. For example:
        Incorrect type: got: <class 'int'>, expected Card object, card not
        added

        Parameters: a_card(unknown type) input parameter to validate.

        Returns boolean (True if instance of card, False otherwise)
        """
        try:
            if isinstance(a_card, Card) == False:
                raise TypeError()
        except:
            excp = "Incorrect type: got: {0}, expected Card object".\
                    format(type(a_card))
            excp += ", card not added"
            print(excp)
            return False
        return True
