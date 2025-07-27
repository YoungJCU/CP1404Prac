from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi that includes fanciness and a flagfall."""

    flagfall = 4.50  # Class-level constant for all SilverServiceTaxis

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Override the price_per_km for this instance based on fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string representation of the SilverServiceTaxi with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
