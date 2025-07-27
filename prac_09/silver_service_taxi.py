from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi that includes fanciness and a flagfall."""

    flagfall = 4.50  # Additional fixed cost for each fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale price per km for this particular instance
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare including flagfall and distance cost."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation of the SilverServiceTaxi with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

