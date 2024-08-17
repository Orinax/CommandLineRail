from rich.table import Table


def create_welcome_card():
    table = Table(title="Command Line Rail", show_header=True, header_style="bold magenta")
    table.add_column("Welcome! You are the new conductor for Command Line Rail!", justify="center")
    table.add_row("Please answer the question prompts as you conduct your trains.", style="bold red")
    table.add_row("You are welcome to run the trains until you get tired and are ready to go home.", style="bold red")

    return table


def create_exit_card():
    table = Table(title="Command Line Rail", show_header=True, header_style="bold magenta")
    table.add_column("Thank you for being today's conductor for Command Line Rail!", justify="center")
    table.add_row("We hope you enjoyed watching the trains run!", style="bold red")
    table.add_row("You are welcome to come back any time and run more trains!", style="bold red")

    return table


def create_table(trains):
    table = Table(title="Train Tables")
    table.add_column("Train Name", style="green", justify="center")
    table.add_column("Current Station", style="green", justify="center")
    table.add_column("Destination", style="green", justify="center")
    table.add_column("Travel Distance", style="green", justify="center")

    for train in trains.values():
        table.add_row(
            str(train.name),
            str(train.current_station.name),
            str(train.current_destination.name),
            str(train.distance_to_destination),
        )

    return table
