matches = [
    {'teams': ['Qatar', 'Ecuador'], 'result': {'winner': 'Ecuador', 'score': '2-0'}},
    {'teams': ['England', 'Iran'], 'result': {'winner': 'England', 'score': '6-2'}},
    {'teams': ['Senegal', 'Netherlands'], 'result': {'winner': 'Netherlands', 'score': '2-0'}},
    {'teams': ['USA', 'Wales'], 'result': {'winner': 'Draw', 'score': '1-1'}},
    {'teams': ['Argentina', 'Saudi Arabia'], 'result': {'winner': 'Saudi Arabia', 'score': '2-1'}},
    {'teams': ['Denmark', 'Tunisia'], 'result': {'winner': 'Draw', 'score': '0-0'}},
    {'teams': ['Mexico', 'Poland'], 'result': {'winner': 'Draw', 'score': '0-0'}},
    {'teams': ['France', 'Australia'], 'result': {'winner': 'France', 'score': '4-1'}},
    {'teams': ['Denmark', 'France'], 'result': {'winner': 'France', 'score': '2-1'}},
    {'teams': ['Saudi Arabia', 'Poland'], 'result': {'winner': 'Poland', 'score': '2-0'}},
    {'teams': ['Argentina', 'Mexico'], 'result': {'winner': 'Argentina', 'score': '2-0'}},
    {'teams': ['Australia', 'Tunisia'], 'result': {'winner': 'Australia', 'score': '1-0'}},
    {'teams': ['Poland', 'Argentina'], 'result': {'winner': 'Argentina', 'score': '2-0'}},
    {'teams': ['France', 'Tunisia'], 'result': {'winner': 'Tunisia', 'score': '1-0'}},
    {'teams': ['Australia', 'Denmark'], 'result': {'winner': 'Australia', 'score': '1-0'}},
    {'teams': ['Japan', 'Costa Rica'], 'result': {'winner': 'Costa Rica', 'score': '1-0'}},
    {'teams': ['Spain', 'Germany'], 'result': {'winner': 'Spain', 'score': '1-0'}},
    {'teams': ['Japan', 'Spain'], 'result': {'winner': 'Japan', 'score': '2-1'}},
    {'teams': ['Costa Rica', 'Germany'], 'result': {'winner': 'Germany', 'score': '4-2'}},
    {'teams': ['South Korea', 'Portugal'], 'result': {'winner': 'South Korea', 'score': '2-1'}},
    {'teams': ['Ghana', 'Uruguay'], 'result': {'winner': 'Uruguay', 'score': '2-0'}},
    {'teams': ['Cameroon', 'Brazil'], 'result': {'winner': 'Cameroon', 'score': '1-0'}},
    {'teams': ['Serbia', 'Switzerland'], 'result': {'winner': 'Switzerland', 'score': '3-2'}},
    {'teams': ['Netherlands', 'USA'], 'result': {'winner': 'Netherlands', 'score': '3-1'}},
    {'teams': ['Argentina', 'Australia'], 'result': {'winner': 'Argentina', 'score': '2-1'}},
    {'teams': ['France', 'Poland'], 'result': {'winner': 'France', 'score': '3-1'}},
    {'teams': ['England', 'Senegal'], 'result': {'winner': 'England', 'score': '3-0'}},
    {'teams': ['Japan', 'Croatia'], 'result': {'winner': 'Draw', 'score': '1-1'}},
    {'teams': ['Brazil', 'South Korea'], 'result': {'winner': 'Brazil', 'score': '4-1'}},
    {'teams': ['Morocco', 'Spain'], 'result': {'winner': 'Draw', 'score': '0-0'}},
    {'teams': ['Portugal', 'Switzerland'], 'result': {'winner': 'Portugal', 'score': '6-1'}},
    {'teams': ['Argentina', 'Netherlands'], 'result': {'winner': 'Draw', 'score': '2-2'}},
    {'teams': ['Croatia', 'Brazil'], 'result': {'winner': 'Draw', 'score': '1-1'}},
    {'teams': ['Morocco', 'Portugal'], 'result': {'winner': 'Morocco', 'score': '1-0'}},
    {'teams': ['France', 'England'], 'result': {'winner': 'France', 'score': '2-1'}},
    {'teams': ['Argentina', 'Croatia'], 'result': {'winner': 'Argentina', 'score': '3-0'}},
    {'teams': ['France', 'Morocco'], 'result': {'winner': 'France', 'score': '2-0'}},
    {'teams': ['Croatia', 'Morocco'], 'result': {'winner': 'Croatia', 'score': '2-1'}},
    {'teams': ['Argentina', 'France'], 'result': {'winner': 'Argentina', 'score': '3-3'}}
]

players = {
    'Argentina': [('Lionel Messi', 7), ('Julian Alvarez', 4), ('Angel Di Maria', 2), ('Lautaro Martinez', 2), ('Enzo Fernandez', 1)],
    'France': [('Kylian Mbappe', 8), ('Olivier Giroud', 4), ('Antoine Griezmann', 3), ('Adrien Rabiot', 2), ('Marcus Thuram', 1)],
    'Brazil': [('Neymar', 6), ('Richarlison', 3), ('Vinicius Jr.', 2), ('Raphinha', 1), ('Lucas Paqueta', 1)],
    'England': [('Harry Kane', 6), ('Bukayo Saka', 3), ('Raheem Sterling', 2), ('Jude Bellingham', 1), ('Phil Foden', 1)],
    'Netherlands': [('Cody Gakpo', 3), ('Memphis Depay', 3), ('Denzel Dumfries', 2), ('Steven Bergwijn', 1), ('Luuk de Jong', 1)],
    'Morocco': [('Youssef En-Nesyri', 2), ('Hakim Ziyech', 2), ('Achraf Hakimi', 1), ('Sofiane Boufal', 1), ('Romain Saiss', 1)],
    'Croatia': [('Luka Modric', 2), ('Ivan Perisic', 2), ('Andrej Kramaric', 2), ('Mario Pasalic', 1), ('Bruno Petkovic', 1)],
    'Portugal': [('Cristiano Ronaldo', 4), ('Bruno Fernandes', 3), ('Joao Felix', 2), ('Rafael Leao', 2), ('Bernardo Silva', 1)],
    'Germany': [('Kai Havertz', 3), ('Ilkay Gundogan', 2), ('Thomas Muller', 2), ('Leroy Sane', 1), ('Jammy Musiala', 1)],
    'Spain': [('Alvaro Morata', 3), ('Dani Olmo', 2), ('Marco Asensio', 1), ('Ferran Torres', 1), ('Pedri', 1)],
    'Australia': [('Mathew Leckie', 2), ('Craig Goodwin', 2), ('Mitchell Duke', 1), ('Awer Mabil', 1), ('Aaron Mooy', 1)],
    'USA': [('Christian Pulisic', 1), ('Tim Weah', 1), ('Brenden Aaronson', 1), ('Haji Wright', 1), ('Giovanni Reyna', 1)],
    'Senegal': [('Ismaila Sarr', 2), ('Kouadio Kone', 2), ('Sadio Mane', 1), ('Bamba Dieng', 1), ('Idrissa Gueye', 1)],
    'Poland': [('Robert Lewandowski', 2), ('Piotr Zielinski', 2), ('Jakub Kaminski', 1), ('Kamil Grosicki', 1), ('Karol Swiderski', 1)],
    'Saudi Arabia': [('Saleh Al-Shehri', 1), ('Salman Al-Faraj', 1), ('Firas Al-Buraikan', 1), ('Mohammed Al-Owais', 1), ('Yasser Al-Shahrani', 1)],
    'Tunisia': [('Wahbi Khazri', 1), ('Youssef Msakni', 1), ('Anis Ben Slimane', 1), ('Ellyes Skhiri', 1), ('Hannibal Mejbri', 1)],
}

goals = {}
matches_played = {}
matches_won = {}

for match in matches:
    team1 = match['teams'][0]
    team2 = match['teams'][1]
    result = match['result']

    
    if team1 not in matches_played:
        matches_played[team1] = 0
    if team2 not in matches_played:
        matches_played[team2] = 0
    
    matches_played[team1] = matches_played[team1]+ 1
    matches_played[team2] =  matches_played[team2]+1
    
    if team1 not in matches_won:
        matches_won[team1] = 0
    if team2 not in matches_won:
        matches_won[team2] = 0
    
    if result['winner'] == team1:
        matches_won[team1] =matches_won[team1]+ 1
    elif result['winner'] == team2:
        matches_won[team2] = matches_won[team2]+ 1
    
    if team1 not in goals:
        goals[team1] = 0
    if team2 not in goals:
        goals[team2] = 0
    
    score1, score2 = map(int, result['score'].split('-'))
    goals[team1] =goals[team1]+ score1
    goals[team2] =goals[team2]+ score2

def total_matches_played(team_name):
    return matches_played.get(team_name, 0)

def top_players(team_name):
    return players.get(team_name, [])

def total_matches_won(team_name):
    return matches_won.get(team_name, 0)

def print_team_stats(team_name):
    print(f"Total matches played by {team_name}: {total_matches_played(team_name)}")
    print(f"Total matches won by {team_name}: {total_matches_won(team_name)}")
    print(f"Top players of {team_name}:")
    print("##########################################################")
    for player, goals in top_players(team_name):
       print("  " + player + ": " + str(goals) + " goals")


print_team_stats('Argentina')
# print_team_stats('France')
# print_team_stats('Brazil')
