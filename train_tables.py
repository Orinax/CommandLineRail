import locale

from rich.table import Table


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def create_welcome_card():
    table = Table(title="Command Line Rail", show_header=True, header_style="bold magenta")
    table.add_column("Welcome! You are the new conductor for Command Line Rail!", justify="center")
    table.add_row("Please answer the question prompts as you conduct your trains.", style="bold red")
    table.add_row("You are welcome to run the trains until you get tired and are ready to go home.", style="bold red")
    return table


def create_exit_card(conductor):
    table = Table(title="Command Line Rail", show_header=True, header_style="bold magenta")
    table.add_column(f"Thank you {conductor.name}, for being today's conductor for Command Line Rail!", justify="center")
    table.add_row("We hope you enjoyed watching the trains run!", style="bold red")
    table.add_row("You are welcome to come back any time and run more trains!", style="bold red")
    table.add_row(f"You earned a total of {str(locale.currency(conductor.total_earnings, grouping=True))},", style="bold green")
    table.add_row(f"and you transported a total of {conductor.passengers_transported} passengers.", style="bold green")
    return table


def create_conductor_table(conductor):
    table = Table(title="Conductor Profile", show_header=True, header_style="bold magenta")
    table.add_column("Conductor Name", justify="center")
    table.add_column("Total Earnings", justify="center")
    table.add_column("Passengers Transported", justify="center")
    table.add_row(
        str(conductor.name),
        str(locale.currency(conductor.total_earnings, grouping=True)),
        str(conductor.passengers_transported),
    style="bold green")
    return table


def create_train_table(trains):
    table = Table(title="Train Tables")
    table.add_column("Train Name", style="green", justify="center")
    table.add_column("Current Station", style="green", justify="center")
    table.add_column("Destination", style="green", justify="center")
    table.add_column("Travel Distance", style="green", justify="center")
    table.add_column("Passengers Onboard", style="green", justify="center")

    for train in trains.values():
        table.add_row(
            str(train.name),
            str(train.current_station.name),
            str(train.current_destination.name),
            f"{str(train.distance_to_destination)} km",
            str(train.num_current_passengers),
        )
    return table
