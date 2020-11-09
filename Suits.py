from Base_Card import *

class Warrior_Card(Card):
    """ This class represents all cards belonging to Warriors of Marina.
    Inherits from the Card class """

    # Class Attributes
    suit = "WM"
    chant = "Marina before all!"
    traitor_offset = 5
    special_card_bonus = 10
    suit_comp = [warrior_ordinary, warrior_specials, warrior_leader]

    # Class Methods
    def get_skill(self, other_card):
        """ Calculates the skill of self, given the other_card instance.
        other_card is a different card from any suit. Note that you should be
        using the traitor_offset, which is the suit bonus of 'WM' """
        skill_lvl = self.number
        if self.card_type == "special":
            skill_lvl += Warrior_Card.special_card_bonus
        if other_card.suit in ["DC", "SS"] :
            return skill_lvl + Warrior_Card.traitor_offset
        else:
            return skill_lvl

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
        if self.card_type == "special":
            if other_card.number <= 10:
                return 0
            else:
                return self.number
        elif self.card_type == "ordinary":
            skill = ((self.number) ** 2) / 4
            return skill
        else: # self.card_type == "Leader"
            return self.number

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
        if other_card.suit != "SS":
            if self.card_type in ["ordinary", "special"]:
                return Secret_Card.secret_offset - self.number
            else: # self.card_type == "Leader"
                return self.number
        else:
            return self.number

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
        suit bonus of Yuxuan's Emissaries."""
        if self.card_type == "ordinary":
            return self.number * Yuxuan_Card.ord_mult
        elif self.card_type == "special":
            skill = self.number * Yuxuan_Card.spe_mult
            if other_card.suit == "DC":
                return skill + Yuxuan_Card.dragon_fear_offset
            else:
                return skill
        else: # self.card_type == "Leader"
            return self.number
