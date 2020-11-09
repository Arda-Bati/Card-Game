from Base_Card import *

class Warrior_Card(Card):
    """ This class represents all cards belonging to Warriors of Marina.
    Inherits from the Card class """

    # Class Attributes
    suit = "WM"
    chant = "Marina before all!"
    traitor_offset = 5
    suit_comp = [warrior_ordinary, warrior_specials, warrior_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is a different card from any suit. Note that you should be
        using the traitor_offset, which is the suit bonus of 'WM' """
        ## YOUR CODE IS HERE ##

class Dragon_Card(Card):
    """ This class represents all cards belonging to Dragon's Children.
    Inherits from the Card class """

    # Class Attributes
    suit = "DC"
    chant = "All hail the Recursive Dragon!"
    suit_comp = [dragon_ordinary, dragon_specials, dragon_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Notice the skill
        calculations will be different for different card types (special,
        ordinary, leader)"""
        ## YOUR CODE IS HERE ##

class Secret_Card(Card):
    """ This class represents all cards belonging to Secret Strikers.
    Inherits from the Card class """

    # Class Attributes
    suit = "SS"
    chant = "We shall strike again!"
    suit_comp = [secret_ordinary, secret_specials, secret_leader]
    secret_offset = 12

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Notice you should
        be using the secret_offset variable in the calculations. Also keep in
        mind the suit bonus of the Secret Strikers. """
        ## YOUR CODE IS HERE ##

class Yuxuan_Card(Card):
    """ This class represents all cards belonging to Yuxuan's Emissaries.
    Inherits from the Card class """

    # Class Attributes
    suit = "YE"
    chant = "I am the Piazza!"
    suit_comp = [yuxuan_ordinary, yuxuan_specials, yuxuan_leader]
    ord_mult = 0.8
    spe_mult = 4
    dragon_fear_offset = -10

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is another card instance of any suit. Keen in mind that
        different rules apply for different card types. Also keep in mind the
        suit bonus of Yuxuan's Emissaries (use dragon_fear_offset for it)."""
        ## YOUR CODE IS HERE ##
