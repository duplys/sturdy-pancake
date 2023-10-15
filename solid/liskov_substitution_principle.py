"""
Code illustrating the Liskov substitution principle (soLid).
"""

from random import randint

class Ship():
    """Type class."""

    def move(self, num):
        """Moving the ship."""
        print(f"Aye aye! Moving {num} squares")

class Carrier(Ship):
    """Subtype class that inherits from Ship."""

    def move(self, num):
        """Moving the ship."""
        print(f"Carrier moves {num} squares ...")

class Corvette(Ship):
    """Another subtype class that inherits from Ship"""

    def move(self, num):
        """Moving the ship."""
        print(f"Corvette moves {num} squares ...")


def make_move_v1(ship_array):
    """Roll a dice and move the ships.
    
        This function does not utilize the Liskov substitution principle.

        ship_array (array): An array of ships of type Carrier or Corvette
    """

    for s in ship_array:
        dist = randint(0,6)
        if type(s) == Carrier:
            s.move(dist)
        if type(s) == Corvette:
            s.move(dist)


def make_move_v2(ship_array: Ship):
    """Roll a dice and move the ships.
    
        This function utilizes Liskov substitution principle.

        ship_array (array): An array of ships of type Carrier or Corvette
    """

    for s in ship_array:
        dist = randint(0,6)
        s.move(dist)



ships =[Carrier(), Corvette()]
make_move_v1(ships)
make_move_v2(ships)


#move_ship(Carrier)
#move_ship(Corvette)
