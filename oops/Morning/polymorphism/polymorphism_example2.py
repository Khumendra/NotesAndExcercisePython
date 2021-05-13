# Polymorphism: Duck Typing
print()

class Worker(object):

    def work(self):
        print("Working")

    def perform_task(self):
        print("Performing Task:", end=' ')
        self.work()


class DeliveryMan(Worker):
    def work(self):
        print("Delivering Good!")


class LumberJack(Worker):
    def work(self):
        print("Cutting Wood!")


deliveryMan = DeliveryMan()
lumberJack = LumberJack()

deliveryMan.perform_task()
lumberJack.perform_task()

