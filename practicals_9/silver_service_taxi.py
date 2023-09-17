from practicals_9.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagella = 4.50

    def __init__(self, name, fuel, fanciness=1.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        return f"{super().__str__()} plus flag-fall of ${self.flagella:,.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagella
