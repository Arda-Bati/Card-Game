"""
Tutor Fighter Card Game data generation.
"""

# Beginning and ending of ordinary card numbers
ORD_BEG = 2
ORD_END = 10
full_deck = []

# Warriors of Marina, Dragon's Children, Secret Strikers, Yuxuan's Emissaries
suits = ["WM", "DC", "SS", "YE"]
ordinary_names = ["Warrior", "Dragon", "Secret", "Emissary"]

# Generating ordinary cards
all_ordinaries = []
for suit_indx, ord_name in enumerate(ordinary_names):
    ordinaries = []
    for i in range(ORD_BEG, ORD_END + 1):
        name = "{0} {1}".format(ord_name, i)
        suit = suits[suit_indx]
        ordinaries.append((name, suit))
    full_deck.extend(ordinaries)
    all_ordinaries.append(ordinaries)

# Creating the named ordinary variables for each suit
warrior_ordinary = all_ordinaries[suits.index("WM")]
dragon_ordinary  = all_ordinaries[suits.index("DC")]
secret_ordinary  = all_ordinaries[suits.index("SS")]
yuxuan_ordinary  = all_ordinaries[suits.index("YE")]

# Creating the named special variables for each suit
warrior_specials = [("Sudi the Sincere 11", "WM"),
                    ("Prem the Persistent 12", "WM"),
                    ("Jonathan the Judge 13", "WM")]

dragon_specials   = [("Etsu the Earnest 30", "DC"),
                     ("Chase the Candid 35", "DC"),
                     ("Nabi the Noble 40", "DC")]

secret_specials = [("Iman the Impeccable -10", "SS"),
                   ("Aaron the Avenger -15", "SS"),
                   ("Wesley the Wrecker -20", "SS")]

yuxuan_specials  = [("Emissary 11", "YE"),
                    ("Emissary 12", "YE"),
                    ("Emissary 13", "YE")]

full_deck.extend(warrior_specials)
full_deck.extend(dragon_specials)
full_deck.extend(secret_specials)
full_deck.extend(yuxuan_specials)

# Creating the named leader variables for each suit
warrior_leader = [("Marina the Marvel 50", "WM")]
dragon_leader  = [("Arda the Architect 100", "DC")]
secret_leader  = [("Cecilia the Contender of Haku 90", "SS")]
yuxuan_leader  = [("Yuxuan the Youthful 80", "YE")]

full_deck.extend(warrior_leader)
full_deck.extend(dragon_leader)
full_deck.extend(secret_leader)
full_deck.extend(yuxuan_leader)

# Sorting the deck according to the order of explanation in the write-up
full_deck.sort(key = lambda x: suits.index(x[1]))
# print(len(full_deck))
# print(full_deck)
