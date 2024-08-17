import random

random_locations = [0]
for i in range(5):
    random_locations.append(random.randint(50,1000))

station_names = ["Central Station", "South Station", "West Station", "King Station", "Amazon Heights", "Empire Flats"]


class Station:
    def __init__(self, name, location, freight=0, passengers=0):
        """Initialize a station object."""
        self.name = name
        self.location = location
        self.freight = freight
        self.passengers = passengers
