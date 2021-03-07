from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping: Topping):
        if topping.weight + self.calculate_total_weight() > self.toppings_capacity:
            # if len(self.__toppings) >= self.__toppings_capacity[topping]:
            raise ValueError('Not enough space for another topping')

        # if topping not in self.__toppings:
        #     self.__toppings[topping] = 0
        # self.__toppings[topping] -= topping.weight
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            return

        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        # total_weight = 0
        # for (k, v) in self.__toppings.items():
        #     total_weight += v
        # return total_weight
        return sum([t for t in self.toppings.values()])
