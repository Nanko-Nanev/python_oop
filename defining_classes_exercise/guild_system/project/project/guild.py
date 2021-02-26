from project.player import Player


class Guild:
    def __init__(self, name):
        self.guild_name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.list_of_players.append(player)
        player.guild = self.guild_name
        return f"Welcome player {player.name} to the guild {self.guild_name}"

    def kick_player(self, player_name):
        if player_name not in self.list_of_players:
            return f"Player {player_name} is not in the guild."

        self.list_of_players.remove(player_name)
        Player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    # def guild_info(self):
    #     res = f'Guild: {self.guild_name}\n'
    #     res2 = []
    #     for play_er in self.list_of_players:
    #         res2.append(f"{Player.player_info(play_er)}")
    #     res += ["\n".join(str(el)) for el in res2]
    #     return res
    def guild_info(self):
        result = f"Guild: {self.guild_name}\n"
        for play_er in self.list_of_players:
            result += f"{play_er.player_info()}"
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
