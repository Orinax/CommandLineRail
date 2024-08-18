import time

from train_tables import create_conductor_table


class Conductor:

    def __init__(self, is_conducting=True, trains_are_running=True, total_earnings=0, passengers_transported=0):
        self.is_conducting = is_conducting
        self.trains_are_running = trains_are_running
        self.total_earnings = total_earnings
        self.passengers_transported = passengers_transported


    def begin_conducting(self):
        making_decision = True

        while making_decision:
            conductors_decision = input("Would you like to begin running the trains for today? (y/n) ")
            if conductors_decision.lower() == 'y':
                break
            elif conductors_decision.lower() == 'n':
                self.is_conducting = False
                making_decision = False
            else:
                print("I didn't understand that. Please try again.")


    def handle_all_trains(self, trains, stations, create_table, console, run_the_trains, os):
        if self.trains_are_running:
            for station in stations.values():
                station.get_passengers()

            for train in trains.values():
                train.choose_destination(stations)
                train.calculate_travel_distance()
                self.total_earnings += train.pick_up_passengers(stations)

            current_table = create_table(trains)
            conductor_table = create_conductor_table(self)
            console.print(current_table)
            console.print(conductor_table)
            print("Press \"Ctrl+c\" at any time to stop the trains.")

            # Move the trains
            run_the_trains(trains)

            for train in trains.values():
                train.update_current_station()
                self.passengers_transported += train.let_passengers_off()

            print("Please mind the gap as you disembark...")
            time.sleep(3)
            print("ALL ABOARD!")
            time.sleep(2)
            os.system('cls||clear')
        else:
            print("All trains have stopped.")
            # In the future, add access to a menu that will allow the conductor to manage the trains while
            # they are at a station.


    def pause_all_trains(self):
        conductor_input = input("Would you like to pause all trains? (y/n) ")
        if conductor_input.lower() == 'y':
            self.trains_are_running = False
        elif conductor_input.lower() == 'n':
            self.trains_are_running = True
        else:
            print("I didn't understand that. Please try again.")


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
