from abc import ABC, abstractmethod


class BaseFish(ABC, abstractmethod):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if self.price <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.price = value
    
    @property
    def species(self):
        return self.species
    
    @species.setter
    def species(self, value):
        if self.species == "":
            raise ValueError("Fish species cannot be an empty string.")
        self.species = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if self.name == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.name = value

    def eat(self):
        self.size += 5
