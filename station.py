import random


class Station:
    def __init__(self, name, location, freight=0, passengers=0):
        """Initialize a station object."""
        self.name = name
        self.location = location
        self.freight = freight
        self.passengers = passengers


    def get_passengers(self):
        self.passengers += random.randrange(0, 5)