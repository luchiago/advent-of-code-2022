MAX_SIZE = 25
MOVEMENT_QTE_IDX = 1
MOVEMENT_FROM_IDX = 3
MOVEMENT_TO_IDX = 5

def queue_pkgs(list_of_pkgs_indexes: list):
    sequence = list_of_pkgs_indexes.pop()
    organized = {obj[0]: [] for obj in sequence}
    for obj in list_of_pkgs_indexes:
        for o in obj:
            organized[o[0]].append(o[1])
    organized_with_indexes = {}
    i = 0
    for key, value in organized.items():
        value.reverse()
        organized_with_indexes[i] = value
        i += 1
    return organized_with_indexes

def make_movements(supplies: dict, movements: list, dequeue: bool = True):
    for movement in movements:
        qte = int(movement[MOVEMENT_QTE_IDX])
        from_stack = int(movement[MOVEMENT_FROM_IDX]) - 1
        to_stack = int(movement[MOVEMENT_TO_IDX]) - 1

        items = []
        for i in range(qte):
            items.append(supplies[from_stack].pop())

        items.reverse()

        if dequeue:
            for i in range(qte):
                supplies[to_stack].append(items.pop())
        else:
            supplies[to_stack] += items

    return supplies

def make_movements_2(supplies: dict, movements: list):
    return make_movements(supplies, movements, dequeue=False)

def get_message(supplies: dict):
    message = ''
    for value in supplies.values():
        letter = value.pop()
        message += letter
    return message

def organize_supplies(line: str):
    indexes = []
    for i, l in enumerate(line):
        if l.isalnum():
            index = i - 1
            indexes.append((index, l))
    return indexes


def process(lines: list):
    supplies = []
    movements = []

    for line in lines:
        if line == '\n':
            supplies = queue_pkgs(supplies)
            continue
        if line.startswith('move'):
            movements.append(line.strip().split(' '))
        else:
            supplies.append(organize_supplies(line))

    # supplies = make_movements(supplies, movements)

    # Part 2
    supplies = make_movements(supplies, movements, False)
    return get_message(supplies)


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        result = process(lines)
        print(result)


if __name__ == '__main__':
    main()
