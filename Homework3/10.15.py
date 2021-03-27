#Brett Meirhofer 2036955


class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def print_team_status(self):
        self.win_percentage = self.get_win_percentage()
        if(self.win_percentage > .5):
            print("Congratulations, Team {} has a winning average!".format(self.team_name))
        else:
            print("Team {} has a losing average.".format(self.team_name))



if __name__ == '__main__':
    TeamRef = Team()
    TeamRef.team_name = input()
    TeamRef.team_wins = int(input())
    TeamRef.team_losses = int(input())
    TeamRef.print_team_status()

