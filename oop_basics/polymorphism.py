"""
Code illustrating polymorphism, in particular, subtyping polymorphism
used in Liskov substitution principle.
"""

class Ship():
    """Type class."""

    def move(self):
        """Moving the ship."""
        print("Aye aye!")

class Carrier(Ship):
    """Subtype class that inherits from Ship."""

    def move(self):
        """Moving the ship."""
        print("I'll crush ye barnacles!")

class Corvette(Ship):
    """Another subtype class that inherits from Ship"""

    def move(self):
        """Moving the ship."""
        print("Shiver me timbers!")


def move_ship(ship):
    """This function uses subtyping."""
    ship.move(ship)


move_ship(Carrier)
move_ship(Corvette)
