import time

from train_tables import create_conductor_table


class Conductor:

    def __init__(self, name="Bob", is_conducting=True, trains_are_running=True,
                 total_earnings=0, passengers_transported=0):
        self.name = name
        self.is_conducting = is_conducting
        self.trains_are_running = trains_are_running
        self.total_earnings = total_earnings
        self.passengers_transported = passengers_transported
        self.ticket_price = 2.15


    def choose_name(self):
        choosing_name = True

        while choosing_name:
            name = input("What is your name? ")
            check_name = input(f"Is {name} correct? (y/n) ")
            if check_name.lower() == 'y':
                self.name = name
                choosing_name = False
            else:
                print("Okay. Let's try again.")


    def begin_conducting(self):
        making_decision = True

        while making_decision:
            conductors_decision = input(f"Would you like to begin running the trains for today {self.name}? (y/n) ")
            if conductors_decision.lower() == 'y':
                break
            elif conductors_decision.lower() == 'n':
                self.is_conducting = False
                making_decision = False
            else:
                print("I didn't understand that. Please try again.")


    def handle_all_trains(self, trains, stations, display_tables, create_table, console, run_the_trains, os):
        if self.trains_are_running:
            passengers_embarking = 0
            passengers_disembarking = 0

            for station in stations.values():
                station.get_passengers()

            for train in trains.values():
                train.choose_destination(stations)
                train.calculate_travel_distance()
                passengers_embarking += train.pick_up_passengers(stations)

            display_tables(self, trains, console, create_table, passengers_embarking)

            # Move the trains
            run_the_trains(self, console, create_table, display_tables, trains, os, passengers_embarking)

            if self.is_conducting:
                for train in trains.values():
                    train.update_current_station()
                    num_passengers_getting_off = train.let_passengers_off()
                    passengers_disembarking += num_passengers_getting_off

                self.total_earnings += passengers_embarking * self.ticket_price
                self.passengers_transported += passengers_disembarking

                print(f"Please mind the gap as you disembark... ({passengers_disembarking} passenger(s) disembarked)")
                time.sleep(3)
                print("ALL ABOARD!")
                time.sleep(2)
                os.system('cls||clear')
            else:
                os.system('cls||clear')

        else:
            print("All trains have stopped.")
            # In the future, add access to a menu that will allow the conductor to manage the trains while
            # they are at a station.


    def stop_conducting(self):
        """The conductor can 'stop conducting' when he is ready to quit working for the day, and all trains will stop
        running. This will cause the program to end."""
        making_decision = True

        while making_decision:
            conductors_decision = input("Would you like to continue running all the trains? (y/n) ")
            if conductors_decision.lower() == 'y':
                self.is_conducting = True
                making_decision = False
            elif conductors_decision.lower() == 'n':
                self.is_conducting = False
                making_decision = False
            else:
                print("I didn't understand that. Please try again.")
