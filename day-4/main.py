def check_contains(p1: str, p2: str, overlap: bool = False):
    p1 = p1.split('-')
    p2 = p2.split('-')
    p1 = range(int(p1[0]), int(p1[1]) + 1)
    p2 = range(int(p2[0]), int(p2[1]) + 1)
    return any(p in p1 for p in p2) if overlap else all(p in p1 for p in p2)


def process(pairs: list, overlap: bool = False):
    count = 0
    for line in pairs:
        pair1, pair2 = line.split(',')
        pair1_contains_pair_2 = check_contains(pair1, pair2, overlap)
        pair2_contains_pair_1 = check_contains(pair2, pair1, overlap)
        if pair1_contains_pair_2 or pair2_contains_pair_1:
            count += 1
    return count

def main(pairs: list = None):
    if not pairs:
        with open('input.txt', 'r') as f:
            pairs = [l.strip() for l in f]

    result = process(pairs, True)
    print(result)

if __name__ == '__main__':
    main()
