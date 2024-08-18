import time

from rich.progress import Progress


def run_the_trains(trains):
    # Move the trains
    with Progress() as progress:
        train0 = progress.add_task(f"[blue]{trains['Train 0'].name}...[/]",
                                   total=trains['Train 0'].distance_to_destination)
        train1 = progress.add_task(f"[yellow]{trains['Train 1'].name}...[/]",
                                   total=trains['Train 1'].distance_to_destination)
        train2 = progress.add_task(f"[magenta]{trains['Train 2'].name}...[/]",
                                   total=trains['Train 2'].distance_to_destination)
        while not progress.finished:
            progress.update(train0, advance=trains['Train 0'].speed)
            progress.update(train1, advance=trains['Train 1'].speed)
            progress.update(train2, advance=trains['Train 2'].speed)
            time.sleep(0.01)
