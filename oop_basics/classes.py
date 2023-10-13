"""
Code illustrating basics of OOP.
"""

class Ship():
    """My first ship."""

    def __init__(self, name) -> None:
        self.name = name
        self.crew = []

    def start(self):
        """Public method to start the ship."""
        print(f"Ahoy, sailor! Setting sails on {self.name}!")

    def stop(self):
        """Public method to stop the ship."""
        print("Hold your horses!")

    def onboard_crew(self, crew):
        """Public method to onboard the crew."""
        self.crew = crew

    def report_crew(self):
        """All men on deck!"""
        print(self.crew)

    def disembard_crew(self, reason):
        """Public method to disembard the crew."""
        print(f"Removing crew because of {reason}")
        self.crew = []

    def go_under_deck(self):
        """Things under deck are secret."""
        self.__start_mutiny()

    def __start_mutiny(self):
        """Mutiny!"""
        print("Yo Mr. Bligh, we're going back to Tahiti!")

# Creating instance of class Ship
ship = Ship("Bounty")

# Adding crew and starting the journey
ship.onboard_crew(["Samuel", "Edward", "Anne"])
ship.report_crew()
ship.start()

# Making a stop
ship.disembard_crew("arrival in Tahiti")
ship.onboard_crew(["Samuel", "Edward", "Anne"])
ship.report_crew()
ship.start()

# What is happening here?
ship.go_under_deck()

#ship.__start_mutiny()
# => AttributeError: 'Ship' object has no attribute '__start_mutiny'
