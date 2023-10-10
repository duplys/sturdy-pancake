"""
Code illustrating abstract classes typically used to
define interfaces that instantiatible classes implement.
"""
from abc import ABC, abstractmethod

class ShipBoardingInterface(ABC):
    """Abstract class defining how to board a ship."""

    @abstractmethod
    def jump_on(self):
        """You can jump on every ship."""

    @abstractmethod
    def swim_to(self):
        """You can swim to every ship."""

    @abstractmethod
    def parachute_on(self):
        """You can parachute on (almost?) every ship"""


class CarrierBoarding(ShipBoardingInterface):
    """Class implementing ShipBoardingInterface."""

    def jump_on(self):
        print("Jump!")

    def swim_to(self):
        print("Swim!")

    def parachute_on(self):
        print("Oh boy!")

cbf = CarrierBoarding()
cbf.parachute_on()

#x = ShipBoardingInterface()