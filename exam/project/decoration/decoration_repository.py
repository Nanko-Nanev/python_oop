class DecorationRepository:
    def __init__(self):
        self.decorations = []  # decorations: list – empty list that will contain all decorations (objects).

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        for dec in self.decorations:
            if dec == decoration:
                self.decorations.remove(decoration)
                return True
        return False

    def find_by_type(self, decoration_type: str):
        for dec in self.decorations:
            if dec.__class__.__name__ == decoration_type:
                return dec
        return "None"
