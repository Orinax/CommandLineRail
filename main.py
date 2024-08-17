import time
from conductor import Conductor
from rich.progress import Progress
from settings import create_stations, create_trains, station_names, train_names, train_speeds, random_locations


def main():

    stations = create_stations(station_names, random_locations)
    trains = create_trains(train_names, train_speeds, stations)

    main_conductor = Conductor()
    while main_conductor.is_conducting:

        for train in trains.values():
            train.choose_destination(stations)
            train.calculate_travel_distance()

        # for station in stations.values():
        #     print("--->", station.name, station.location)

        # Move the trains
        with Progress() as progress:
            train0 = progress.add_task(f"[blue]{trains['Train 0'].name}...[/]", total=trains['Train 0'].distance_to_destination)
            train1 = progress.add_task(f"[yellow]{trains['Train 1'].name}...[/]", total=trains['Train 1'].distance_to_destination)
            train2 = progress.add_task(f"[magenta]{trains['Train 2'].name}...[/]", total=trains['Train 2'].distance_to_destination)
            while not progress.finished:
                progress.update(train0, advance=trains['Train 0'].speed)
                progress.update(train1, advance=trains['Train 1'].speed)
                progress.update(train2, advance=trains['Train 2'].speed)
                time.sleep(0.01)

        for train in trains.values():
            train.update_current_station()

        main_conductor.go_home()


if __name__ == "__main__":
    main()
