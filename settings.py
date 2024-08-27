import random

from rich.progress import Progress, ProgressBar

from train import Train
from station import Station


station_names = ["Central Station", "South Station", "West Station", "King Station", "Amazon Heights", "Empire Flats",
                 "Tumblestone Canyon", "Deepslate Docks", "Distant Outpost"]
train_names = ["Electric Blue", "Yellowstone Bullet", "Magenta Magnet", "Crimson Steamer"]
train_speeds = [0.8, 0.7, 0.9, 1.0]
train_colors = ["blue", "yellow", "magenta", "red"]

random_locations = []
for i in range(len(station_names)):
    random_locations.append(random.randint(100,1000))

# Create stations
def create_stations(station_name_list, random_location_list):
    stations = {}
    for index in range(len(station_name_list)):
        stations[station_names[index]] = Station(station_name_list[index], random_location_list[index])
    return stations

# Create trains
def create_trains(train_name_list, train_speed_list, stations, train_color_list):
    trains = {}
    for index in range(len(train_name_list)):
        trains[f"Train {index}"] = Train(train_name_list[index], train_speed_list[index], stations["Central Station"],
                                         stations["Central Station"], train_color_list[index])
    return trains
