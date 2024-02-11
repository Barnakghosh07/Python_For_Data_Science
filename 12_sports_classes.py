import datetime

class CricketPlayer: 
    def __init__(self, fname, lname, birthyear, team) :
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birthyear
        self.team = team
        self.scores = []
    
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)
    
    def __lt__(self, other):
        my_score = self.get_avg_score()
        other_score = other.get_avg_score()
        return my_score<other_score
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, the cricket player from {self.team}'


# here virat is object and CricketPlayer() is class that's we created before 

  
virat = CricketPlayer('virat', 'kohli', 1988, 'india')
virat.add_score(80)
virat.add_score(180)
virat.add_score(0)

print(virat.get_avg_score())


david = CricketPlayer('david', 'warner', 1985, 'australia')
david.add_score(60)
david.add_score(10)
david.add_score(90)

print(david.get_avg_score())

# operator overloading

print(virat)
print(david)