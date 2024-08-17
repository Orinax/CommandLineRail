import time

from conductor import Conductor
from rich.console import Console
from rich.progress import Progress
from settings import create_stations, create_trains, station_names, train_names, train_speeds, random_locations
from train_table import create_welcome_card, create_table, create_exit_card


stations = create_stations(station_names, random_locations)
trains = create_trains(train_names, train_speeds, stations)
welcome_card = create_welcome_card()
exit_card = create_exit_card()
console = Console()


def main():

    console.print(welcome_card)
    main_conductor = Conductor()
    main_conductor.begin_conducting()

    while main_conductor.is_conducting:

        for train in trains.values():
            train.choose_destination(stations)
            train.calculate_travel_distance()

        current_table = create_table(trains)
        console.print(current_table)

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

    console.print(exit_card)


if __name__ == "__main__":
    main()
