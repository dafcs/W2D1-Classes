class Team():
    def __init__(self,team_name,players_list,coach_name):
        self.name = team_name
        self.players = players_list
        self.coach = coach_name
        self.points = 0

    def add_player(self,player_name):
        self.players.append(player_name)

    def has_player(self,player_name):
        return player_name in self.players

    
    def points(self):
        return self.points


    def play_game(self,bool):
        if bool is True:
            self.points = 3

