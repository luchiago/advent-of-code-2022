def process2(line: str):
    return process(line, 14)

def process(line: str, first_marker: int = 4):
    test_marker = []
    word = list(line)
    for i in range(len(word)):
        for letter in word[i:i+first_marker]:
            test_marker.append(letter)
        marker = set(test_marker)
        if len(marker) == first_marker:
            return i + first_marker
        else:
            test_marker = []


def main():
    with open('input.txt', 'r') as f:
        lines = f.readline()
        result = process2(lines)
        print(result)


if __name__ == '__main__':
    main()
