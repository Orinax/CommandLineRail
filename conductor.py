class Conductor:

    def __init__(self, is_conducting=True):
        self.is_conducting = is_conducting


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


    def go_home(self):
        """The conductor can 'Go Home' when he is ready to quit working for the day, and all trains will stop
        running. This will cause the program to end."""
        making_decision = True

        while making_decision:
            conductors_decision = input("Would you like to go home and stop running all the trains? (y/n) ")
            if conductors_decision.lower() == 'y':
                self.is_conducting = False
                making_decision = False
            elif conductors_decision.lower() == 'n':
                self.is_conducting = True
                making_decision = False
            else:
                print("I didn't understand that. Please try again.")
