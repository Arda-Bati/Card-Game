from Data import *

class Card():
    """
    This class is the parent for all other card types. It is not used directly,
    meaning no direct instances of Card will be created. This class includes
    methods which are common among all the derived (child) classes such as
    Dragon_Card. Keep in mind that for an instance of a child class, such as
    dc1 = Dragon_Card("Dragon 2"), isinstance(dc1, Card) == True.
    """
    # Class Attributes
    card_types = ["ordinary", "special", "leader"]

    # Constructor
    def __init__(self, name):
        """ Constructor for Card Class, will be used by all child instances.

        Instance attributes to initialize:
        name(str): Card's name (ie "Warrior 9")
        number(int): Card's number (ie. 9)
        card_type(str): Card's type (ie. "ordinary"). To determine the Card's
        type, you can use the suit & suit_comp variable of the child Classes.

        Parameters:
        name (str): The name of the card. Assume it will be a string.

        Returns: None
        """
        self.name = name
        self.number = int(name.split()[-1])
        card_types = Card.card_types
        card_type = card_types[0]
        for i in range(len(card_types)):
            if (self.name, self.suit) in self.suit_comp[i]:
                card_type = card_types[i]
        self.card_type = card_type

    # Comparators
    def __eq__(self, other):
        """Compares the skill levels of self and another card instance (other).
        All faction related rules are applied during the skill calculations.
        For example Nabi the Noble reduces to 0 skill (forfeits) if the other
        card has a number <= 10.
        Returns True if the final calculated skills are equal. False ow."""
        my_skill = self.get_skill(other)
        other_skill = other.get_skill(self)
        return my_skill == other_skill
    def __ne__(self, other):
        """ Similar to __eq__ compares the skill levels of self and other.
        Returns True if the final calculated skills are not equal. False ow.
        """
        return not self.__eq__(other)
    def __gt__(self, other):
        """Compares skills, returns True if self has higher skill, False ow."""
        my_skill = self.get_skill(other)
        other_skill = other.get_skill(self)
        return my_skill > other_skill
    def __ge__(self, other):
        """Compares skills, greater than or equal to method."""
        return self.__eq__(other) or self.__gt__(other)
    def __lt__(self, other):
        """Compares skills, less than method."""
        return not (self.__eq__(other) or self.__gt__(other))
    def __le__(self, other):
        """Compares skills, less than or equal to method."""
        return self.__eq__(other) or (not self.__gt__(other))

    # String and repr representations
    def __str__(self):
        """ String representation for any derived Card instance. """
        str_form = "Card name: {0}, number: {1}, suit: {2}, card type: {3}"
        str_form = str_form.format(self.name, self.number, self.suit,\
                   self.card_type)
        return str_form
    def __repr__(self):
        """ Repr for any derived Card instance. """
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form
