from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self, comfort=5, price=10):
        super().__init__(comfort, price)
