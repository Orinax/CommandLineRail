from progress.bar import Bar
from time import sleep


class Train:

    def __init__(self, name, is_moving=False, current_station="Central Station", current_destination="N/A",
                 current_speed=0, max_speed=10, num_total_cars=0, num_freight_cars=0, num_passenger_cars=0):
        self.name = name
        self.is_moving = is_moving
        self.current_station = current_station
        self.current_destination = current_destination
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.num_total_cars = num_total_cars
        self.num_freight_cars = num_freight_cars
        self.num_passenger_cars = num_passenger_cars

    def travel(self, time):
        self.is_moving = True
        self.current_speed = self.max_speed

        bar = Bar("Traveling", max=time)
        for i in range(time):
            sleep(0.05)
            bar.next()

        print("Traveling")