import random

from rich.progress import Progress
from progress.bar import Bar
from time import sleep

class Train:

    def __init__(self, name, speed, current_station, current_destination, distance_to_destination=0,
                 num_total_cars=0, num_freight_cars=0, num_passenger_cars=0):
        self.name = name
        self.speed = speed
        self.current_station = current_station
        self.current_destination = current_destination
        self.distance_to_destination = distance_to_destination
        self.num_total_cars = num_total_cars
        self.num_freight_cars = num_freight_cars
        self.num_passenger_cars = num_passenger_cars

    def choose_destination(self, stations):
        possible_destinations = []
        for station in stations.values():
            possible_destinations.append(station)

        if self.current_station in possible_destinations:
            possible_destinations.remove(self.current_station)
        self.current_destination = random.choice(possible_destinations)
        print(f"{self.name} is at {self.current_station.name}, departing for {self.current_destination.name}")


    def calculate_travel_distance(self):
        start = self.current_station.location
        end = self.current_destination.location

        if end > start:
            self.distance_to_destination = end - start
        else:
            self.distance_to_destination = start - end
        print(f"{self.name} will travel {self.distance_to_destination} km")


    def update_current_station(self):
        """After travelling, update current station location with current_destination because the train will
        have now arrived."""
        self.current_station = self.current_destination
        print(f"{self.name} is now at {self.current_station.name}")


    def travel(self, time):
        self.is_moving = True
        self.current_speed = self.max_speed

        bar = Bar("Traveling", max=time)
        for i in range(time):
            sleep(0.05)
            bar.next()

        print("Traveling")