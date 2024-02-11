import datetime

virat = {
    'first_name': 'virat',
    'last_name': 'Kohli',
    'birth_year': 1988,
    'scores': [] 
}


virat['scores'].append(80)
virat['scores'].append(180)
virat['scores'].append(2)

def get_avg_score(player):
   return(sum(player['scores'])/len(player['scores']))

def get_age(player):
   now = datetime.datetime.now()
   return now.year - player['birth_year']
    

# print(get_age(virat))
# print(get_avg_score(virat))






david = {
        'first_name': 'david',
        'last_name': 'warner',
        'birth_year': 1986,
        'scores': [] 
}

david['scores'].append(30)
david['scores'].append(110)
david['scores'].append(78)

print(get_age(david))
print(get_avg_score(david))