from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []  # collection all of the players.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player: Player):
        # p = [p for p in self.players if p.name == player.name][0]
        # if p:
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        try:
            p = [p for p in self.players if p.name == player_name][0]
            res = ""
            if p:
                res = p
                self.players.remove(p)
                return res
        except IndexError:
            return f"Player {player_name} not found"