from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.air_conditioners = True

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, refuel):
        pass


class Car(Vehicle, ABC):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance):
        if self.air_conditioners:
            f_c = self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION
        else:
            f_c = self.fuel_consumption
        if self.fuel_quantity - (f_c * distance) >= 0:
            self.fuel_quantity -= f_c * distance

    def refuel(self, refuel):
        self.fuel_quantity += refuel


class Truck(Vehicle, ABC):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    TANK_HOLE_FUEL_DECREASE = 0.95

    def drive(self, distance):
        if self.air_conditioners:
            f_c = self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION
        else:
            f_c = self.fuel_consumption
        if self.fuel_quantity - (f_c * distance) >= 0:
            self.fuel_quantity -= f_c * distance

    def refuel(self, refuel):
        self.fuel_quantity += refuel * self.TANK_HOLE_FUEL_DECREASE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
