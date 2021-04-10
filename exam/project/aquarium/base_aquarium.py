from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC, abstractmethod):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if self.name == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.name = value

    def calculate_comfort(self):
        comfort = 0
        for dec in self.decorations:
            comfort += dec.comfot
        return comfort

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        self.fish += fish
        return f"Successfully added {self.fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        for f in self.fish:
            if f == fish:
                self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}\n"
        res = []
        for f in self.fish:
            res.append(f.name)
        if res:
            result += f"Fish: {', '.join(res)}\n"
        else:
            result += "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"


