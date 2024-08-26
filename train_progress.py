import time

from rich.progress import Progress
from settings import train_names, train_colors, train_speeds


def run_the_trains(trains):
    # Move the trains
    bars = []
    with Progress() as progress:

        for index in range(len(trains)):
            bar = progress.add_task(f"[{trains[f'Train {index}'].color}]{trains[f'Train {index}'].name}...[/]",
                                                       total=trains[f'Train {index}'].distance_to_destination)
            bars.append(bar)

        while not progress.finished:
            train_num = 0
            for bar in bars:
                progress.update(bar, advance=trains[f'Train {train_num}'].speed)
                time.sleep(0.01)
                train_num += 1
