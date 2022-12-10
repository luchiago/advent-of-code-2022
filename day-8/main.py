def build_forest(trees: list, only_trees: bool = False):
    forest = []
    for tree_line in trees:
        forest.append([int(tree) for tree in tree_line])

    if only_trees:
        return forest

    marked_forest = []
    for i, line in enumerate(forest):
        tmp = []
        for j, column in enumerate(line):
            is_edge = check_edge(i, j, len(forest), len(line))
            tmp.append((column, is_edge))
        marked_forest.append(tmp)

    return marked_forest

def check_edge(i: int, j: int, size_forest: int, size_column: int):
    if i - 1 < 0 or j - 1 < 0:
        return True
    elif i + 1 >= size_forest or j + 1 >= size_column:
        return True
    return False

def check_grid(
    forest: list,
    fixed: int,
    position: int,
    tree: tuple,
    limit: int,
    inverter: bool = False
):
    local_visible = []
    compare = None
    iterate_over = []

    if position > limit:
        iterate_over = reversed(range(limit, position))
    else:
        iterate_over = range(position + 1, limit)

    for index in iterate_over:
        if inverter:
            compare = forest[index][fixed]
        else:
            compare = forest[fixed][index]
        local_visible.append(tree[0] > compare[0])

    return all(local_visible)

def check_visible(forest: list, column: list, tree: tuple, i: int, j: int):
    # Check if is edge
    if tree[1]:
        return 1

    visible = []
    size_column = len(column)
    size_forest = len(forest)

    # Check left
    visible.append(check_grid(forest, i, j, tree, 0))

    # Check right
    visible.append(check_grid(forest, i, j, tree, size_column))

    # Check top
    visible.append(check_grid(forest, j, i, tree, 0, True))

    # Check bottom
    visible.append(check_grid(forest, j, i, tree, size_forest, True))

    return 1 if any(visible) else 0

def process(lines: list):
    forest = build_forest(lines)
    visible = 0

    for i, column in enumerate(forest):
        for j, tree in enumerate(column):
            is_visible = check_visible(
                forest,
                column,
                tree,
                i,
                j
            )
            visible += is_visible
    return visible

def get_score(
    forest: list,
    fixed: int,
    position: int,
    tree: int,
    limit: int,
    inverter: bool = False
):
    view = 0
    compare = None
    iterate_over = []

    if position > limit:
        iterate_over = reversed(range(limit, position))
    else:
        iterate_over = range(position + 1, limit)

    for index in iterate_over:
        if inverter:
            compare = forest[index][fixed]
        else:
            compare = forest[fixed][index]
        if tree > compare:
            view += 1
        elif tree <= compare:
            view += 1
            return view
    return view

def check_score(forest: list, column: list, tree: int, i: int, j: int):
    size_column = len(column)
    size_forest = len(forest)
    score = 1

    # Check left
    score *= get_score(forest, i, j, tree, 0)

    # Check right
    score *= get_score(forest, i, j, tree, size_column)

    # Check top
    score *= get_score(forest, j, i, tree, 0, True)

    # Check bottom
    score *= get_score(forest, j, i, tree, size_forest, True)

    return score


def process_2(lines: list):
    forest = build_forest(lines, True)

    highest = 0

    for i, column in enumerate(forest):
        for j, tree in enumerate(column):
            scenic_score = check_score(
                forest,
                column,
                tree,
                i,
                j,
            )
            if scenic_score > highest:
                highest = scenic_score

    return highest


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        result = process_2(lines)
        print(result)


if __name__ == '__main__':
    main()
