class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(SportsPerson):
    def __init__(self,t_name,p_name,role,goal,match):
        super().__init__(t_name,p_name,role)
        self.goal=goal
        self.match=match
        self.earning_per_match=(self.goal * 1000) + (self.match * 10)
        self.goal_ratio=0
    def calculate_ratio(self):
        self.goal_ratio=self.goal/self.match
    def print_details(self):
        print(f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.match}\nGoal Ratio: {self.goal_ratio}\nMatch Earning: {self.earning_per_match}")
class Manager(SportsPerson):
    def __init__(self,t_name,manager,role,win):
        super().__init__(t_name,manager,role)
        self.win=win
        self.earning_per_match=(self.win * 1000)
    def print_details(self):
        print(f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Win: {self.win} \nMatch Earning: {self.earning_per_match}")
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

