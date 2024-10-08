import os

from conductor import Conductor
from rich.console import Console
from settings import create_stations, create_trains, station_names, train_names, train_speeds, random_locations, \
    train_colors

from train_progress import run_the_trains
from train_tables import create_welcome_card, create_train_table, create_exit_card, display_tables


stations = create_stations(station_names, random_locations)
trains = create_trains(train_names, train_speeds, stations, train_colors)
# bars = create_progress_bars(train_names, train_colors, trains)
main_conductor = Conductor()
welcome_card = create_welcome_card()
console = Console()


def main():

    console.print(welcome_card)
    main_conductor.choose_name()
    main_conductor.begin_conducting()
    os.system('cls||clear')

    while main_conductor.is_conducting:
        main_conductor.handle_all_trains(trains, stations, display_tables, create_train_table, console, run_the_trains, os)

    exit_card = create_exit_card(main_conductor)
    console.print(exit_card)
    input("Press any key to quit.")
    os.system('cls||clear')


if __name__ == "__main__":
    main()
