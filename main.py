import curses
import time
from station import Station, random_locations, station_names
from train import Train, train_names
from alive_progress.styles import showtime

def main():

    # Create stations
    stations = {}
    for index in range(len(station_names)):
        stations[station_names[index]] = Station(station_names[index], random_locations[index])

    # Create trains
    trains = {}
    for index in range(len(train_names)):
        trains[train_names[index]] = Train(train_names[index])

    # Move the trains
    # for train in trains.values():
    #     train.travel(200)
    showtime()

if __name__ == "__main__":
    main()
