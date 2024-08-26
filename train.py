import random


class Train:

    def __init__(self, name, speed, current_station, current_destination, color, distance_to_destination=0,
                 num_total_cars=0, num_freight_cars=0, num_passenger_cars=1, num_current_passengers=0):
        self.name = name
        self.speed = speed
        self.current_station = current_station
        self.current_destination = current_destination
        self.color = color
        self.distance_to_destination = distance_to_destination
        self.num_total_cars = num_total_cars
        self.num_freight_cars = num_freight_cars
        self.num_passenger_cars = num_passenger_cars
        self.num_current_passengers = num_current_passengers
        self.max_passenger_capacity = self.num_passenger_cars * 10


    def choose_destination(self, stations):
        possible_destinations = []
        for station in stations.values():
            possible_destinations.append(station)

        if self.current_station in possible_destinations:
            possible_destinations.remove(self.current_station)
        self.current_destination = random.choice(possible_destinations)
        # print(f"{self.name} is at {self.current_station.name}, departing for {self.current_destination.name}")


    def calculate_travel_distance(self):
        start = self.current_station.location
        end = self.current_destination.location

        if end > start:
            self.distance_to_destination = end - start
        else:
            self.distance_to_destination = start - end
        # print(f"{self.name} will travel {self.distance_to_destination} km")


    def update_current_station(self):
        """After travelling, update current station location with current_destination because the train will
        have now arrived."""
        self.current_station = self.current_destination
        # print(f"{self.name} is now at {self.current_station.name}")


    def pick_up_passengers(self, stations):
        random_num_of_boarders = 0
        num_open_seats = self.max_passenger_capacity - self.num_current_passengers

        if stations[self.current_station.name].passengers > 0 and stations[self.current_station.name].passengers <= num_open_seats:
            random_num_of_boarders = random.randrange(0, stations[self.current_station.name].passengers)
            self.num_current_passengers += random_num_of_boarders
            stations[self.current_station.name].passengers -= random_num_of_boarders
        if stations[self.current_station.name].passengers > num_open_seats:
            random_num_of_boarders = random.randrange(0, num_open_seats)
            self.num_current_passengers += random_num_of_boarders
            stations[self.current_station.name].passengers -= random_num_of_boarders

        return random_num_of_boarders


    def let_passengers_off(self):
         if self.num_current_passengers > 0:
             random_num_of_disembarkers = random.randrange(0, self.num_current_passengers)
             self.num_current_passengers -= random_num_of_disembarkers
             return random_num_of_disembarkers
         else:
             return 0
