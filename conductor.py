class Conductor:

    def __init__(self, is_conducting=True, trains_are_running=True):
        self.is_conducting = is_conducting
        self.trains_are_running = trains_are_running


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
            for train in trains.values():
                train.choose_destination(stations)
                train.calculate_travel_distance()

            current_table = create_table(trains)
            console.print(current_table)
            print("Press \"Ctrl+c\" at any time to stop the trains.")

            # Move the trains
            run_the_trains(trains)

            for train in trains.values():
                train.update_current_station()
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
