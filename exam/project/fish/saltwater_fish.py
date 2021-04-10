from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):  # The SaltwaterFish could only live in SaltwaterAquarium!
    def __init__(self, name: str, species: str, price: float, size: int = 5):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 2

