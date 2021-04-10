from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __int__(self, decorations_repository: DecorationRepository, aquariums):
        self.decorations_repository = decorations_repository
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        pass  # TODO

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = [d for d in self.decorations_repository.decorations if d.decoration_type == decoration_type][0]
        existing_decoration = self.decorations_repository.find_by_type(decoration_type)
        pass  # TODO

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass  # TODO

    def feed_fish(self, aquarium_name: str):
        aquarium_to_find = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
        aquarium_to_find.feed()
        return f"Fish fed: {len(aquarium_to_find.fish)}"

    def calculate_value(self, aquarium_name: str):
        pass  # TODO

    def report(self):
        pass  # TODO