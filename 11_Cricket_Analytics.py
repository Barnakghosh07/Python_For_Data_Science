# d = {
#     'rohit' : [12,10,33,107,130],
#     'shakib' : [13,33,1,35,11]
# }

player_scores = {}
with open ("scores.csv", "r") as f:
    for line in f:
        player, score = line.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]
    

# print(player_scores)

for player,score_list in player_scores.items():
    print(player, score_list)
    min_score = min (score_list)
    max_score = max(score_list)
    avg_score = sum(score_list)/len(score_list)

    print(f"{player} ==> Min: {min_score}, Max: {max_score}, Avg: {avg_score}")