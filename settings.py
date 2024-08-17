import random
from train import Train
from station import Station

random_locations = [0]
for i in range(5):
    random_locations.append(random.randint(50,1000))

station_names = ["Central Station", "South Station", "West Station", "King Station", "Amazon Heights", "Empire Flats"]
train_names = ["Electric Blue", "Yellowstone Bullet", "Magenta Magnet"]
train_speeds = [0.7, 0.5, 0.9]


# Create stations
def create_stations(station_name_list, random_location_list):
    stations = {}
    for index in range(len(station_name_list)):
        stations[station_names[index]] = Station(station_name_list[index], random_location_list[index])
    return stations

# Create trains
def create_trains(train_name_list, train_speed_list, stations):
    trains = {}
    for index in range(len(train_name_list)):
        trains[f"Train {index}"] = Train(train_name_list[index], train_speed_list[index], stations["Central Station"],
                                         stations["Central Station"])
    return trains
