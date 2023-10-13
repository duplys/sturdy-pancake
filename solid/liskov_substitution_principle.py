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


def make_move_bad(ship_array):
    """Roll a dice and move the ships.
    
        This function violates the Liskov substitution principle.

        ship_array (array): An array of ships of types Carrier or Corvette
    """
    
    for s in ship_array:
        dist = randint(0,6)
        if s.isinstance(Carrier):
            s.move(dist)
        if s.isinstance(Corvette):
            s.move(dist)



ships =[Carrier, Corvette]

print(ships)
#move_ship(Carrier)
#move_ship(Corvette)
