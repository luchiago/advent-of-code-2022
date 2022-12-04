import string

ALPHABET = list(string.ascii_letters)

def find_common(item1: str, item2: str):
    return set(item1).intersection(set(item2)).pop()

def find_common_group(item1: str, item2: str, item3: str):
    return list(set(item1) & set(item2) & set(item3)).pop()

def divide_items(rucksack: str):
    rucksack = rucksack.strip()
    rucksack_len = len(rucksack)
    first_half = rucksack[:rucksack_len//2]
    second_half = rucksack[rucksack_len//2:]
    return first_half, second_half

sum_priority = 0

with open('input.txt', 'r') as f:
    i = 0
    group = []
    for line in f:
        group.append(line.strip())
        i += 1
        if i == 3:
            common_item_type = find_common_group(*group)
            sum_priority += ALPHABET.index(common_item_type) + 1
            i = 0
            group = []

print(sum_priority)
