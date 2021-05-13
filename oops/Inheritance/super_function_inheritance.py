class Vehical:
    def start(self):
        print("Starting Engine...")
    def stop(self):
        print("Stopping Engine...")

class TwoWheeler(Vehical):
    def say(self):
        super().start()
        print("I have two wheels")
        super().stop()
    
harley = TwoWheeler()
harley.say()