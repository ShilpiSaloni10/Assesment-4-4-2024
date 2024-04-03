class Vehicle:
    def drive(me):
        print("Driving a vehicle.")

class Car(Vehicle):
    def drive(me):
        print("Driving a car.")

class Truck(Vehicle):
    def drive(me):
        print("Driving a truck.")

class Motorcycle(Vehicle):
    def drive(me):
        print("Riding a motorcycle.")

car = Car()
truck = Truck()
motorcycle = Motorcycle()

car.drive()
truck.drive()
motorcycle.drive()