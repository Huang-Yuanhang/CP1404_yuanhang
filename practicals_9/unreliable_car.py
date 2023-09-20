from random import randint

from car import Car


class UnreliableCar(Car):

    def __init__(self, reliability=0.0, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, {self.reliability}% reliable"

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
