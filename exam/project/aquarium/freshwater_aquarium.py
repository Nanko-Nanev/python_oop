from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str, capacity: int = 50):
        super().__init__(name, capacity)

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self, value):
        self.capacity = value
