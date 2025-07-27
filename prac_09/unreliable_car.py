import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A car that may not always drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability (0 to 100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):

        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0  # Car failed to start