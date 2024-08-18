import os
import time

from conductor import Conductor
from rich.console import Console
from settings import create_stations, create_trains, station_names, train_names, train_speeds, random_locations
from train_progress import run_the_trains
from train_tables import create_welcome_card, create_table, create_exit_card


stations = create_stations(station_names, random_locations)
trains = create_trains(train_names, train_speeds, stations)
main_conductor = Conductor()
welcome_card = create_welcome_card()
exit_card = create_exit_card()
console = Console()


def main():

    console.print(welcome_card)
    main_conductor.begin_conducting()
    os.system('cls||clear')

    while main_conductor.is_conducting:
        try:
            while main_conductor.is_conducting:
                main_conductor.handle_all_trains(trains, stations, create_table, console, run_the_trains, os)
        except KeyboardInterrupt:
            main_conductor.stop_conducting()
            os.system('cls||clear')

    console.print(exit_card)
    time.sleep(4)
    os.system('cls||clear')


if __name__ == "__main__":
    main()
