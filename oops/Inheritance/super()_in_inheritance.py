class Vehicle:
    def start(self):
        print('Starting Engine.')

    def stop(self):
        print("Stopping Engine.")


class TwoWheeler(Vehicle):
    def say(self):
        super().start()
        print('I have 2 wheels.')
        super().stop()


harley = TwoWheeler()
harley.say()
