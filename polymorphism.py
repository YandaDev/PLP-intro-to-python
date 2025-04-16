# BASE CLASS: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):  # Base method for movement behavior
        pass

# CHILD CLASS: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} 🚗: Driving on the road.")

# CHILD CLASS: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} ✈️: Flying through the skies.")

# Create objects 
mercedes = Car("Mercedes Benz")
boeing = Plane("Boeng 737 Max")

# Demonstrate polymorphic behavior with different vehicle types
for vehicle in [mercedes, boeing]:
    vehicle.move()