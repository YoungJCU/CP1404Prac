import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A car that may not always drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability (0 to 100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability."""
        # TODO: Implement actual unreliable logic in final step
        print("Drive attempt (stub) - actual logic will go here.")
        return 0  # Default to not driving
