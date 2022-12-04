most_calories_1st = 0
most_calories_2st = 0
most_calories_3st = 0
calories = 0

with open('input.txt', 'r') as f:
    for line in f:
        if line == '\n':
            if calories > most_calories_1st:
                most_calories_1st = calories
                calories = 0
                continue
            elif calories > most_calories_2st:
                most_calories_2st = calories
                calories = 0
                continue
            elif calories > most_calories_3st:
                most_calories_3st = calories
                calories = 0
                continue
            else:
                calories = 0
        else:
            calories += int(line)

print(most_calories_1st)
print(most_calories_2st)
print(most_calories_3st)
print(most_calories_1st + most_calories_2st + most_calories_3st)
