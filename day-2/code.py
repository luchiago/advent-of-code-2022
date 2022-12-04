# A and X is Rock (1)
# B and Y is Paper (2)
# C and Z is Scissors (3)

# 0 for lost
# 3 for draw
# 6 for win

def match_cases(player1, player2):
    if player1 == 'A':
        if player2 == 'X':
            # Draw
            return 1 + 3
        if player2 == 'Y':
            # Win
            return 2 + 6
        if player2 == 'Z':
            # Lost
            return 3 + 0
    elif player1 == 'B':
        if player2 == 'X':
            # Lost
            return 1 + 0
        if player2 == 'Y':
            # Draw
            return 2 + 3
        if player2 == 'Z':
            # Win
            return 3 + 6
    elif player1 == 'C':
        if player2 == 'X':
            # Win
            return 1 + 6
        if player2 == 'Y':
            # Lost
            return 2 + 0
        if player2 == 'Z':
            # Draw
            return 3 + 3

def match_cases_new_strategy(player1, player2):
    if player2 == 'X':
        # Lose
        if player1 == 'A':
            return match_cases(player1, 'Z')
        if player1 == 'B':
            return match_cases(player1, 'X')
        if player1 == 'C':
            return match_cases(player1, 'Y')
    elif player2 == 'Y':
        # Draw
        if player1 == 'A':
            return match_cases(player1, 'X')
        if player1 == 'B':
            return match_cases(player1, 'Y')
        if player1 == 'C':
            return match_cases(player1, 'Z')
    elif player2 == 'Z':
        # Win
        if player1 == 'A':
            return match_cases(player1, 'Y')
        if player1 == 'B':
            return match_cases(player1, 'Z')
        if player1 == 'C':
            return match_cases(player1, 'X')

score = 0
with open('input.txt', 'r') as f:
    for line in f:
        try:
            player1, player2 = line.split()
            score += match_cases_new_strategy(player1, player2)
        except TypeError:
            print(player1)
            print(player2)
            print(match_cases_new_strategy(player1, player2))
            break

print(score)
