from dataclasses import dataclass, field

@dataclass
class Directory:
    parent_dir: 'Directory' = None
    child_dirs: list['Directory'] = field(default_factory=list)
    files: list[int] = field(default_factory=list)
    total_size: int = 0
    name: str = ''


def find_directory(root: 'Directory', name: str):
    for child_dir in root.child_dirs:
        if child_dir.name == name:
            return child_dir

def create_dir_ref(parent: 'Directory', name: str):
    directory = find_directory(parent, name)
    if directory is None:
        directory = Directory(parent_dir=parent, name=name)
        parent.child_dirs.append(directory)
    return directory

def adjust_total_sizes(directory: 'Directory'):
    for child in directory.child_dirs:
        child = adjust_total_sizes(child)
        directory.total_size += child.total_size
    return directory

def calc_size_dirs(directory: 'Directory', total: int = 0):
    for child in directory.child_dirs:
        child, total = calc_size_dirs(child, total)
        if child.total_size <= 100000:
            total += child.total_size
    return directory, total

def mount_dir_tree(lines: list):
    current_dir = None
    root_dir = None

    for output in lines:
        out = output.split(' ')
        if 'cd' in out:
            directory_name = out[2]
            if directory_name == '..':
                current_dir = current_dir.parent_dir
            else:
                if current_dir is None:
                    directory = Directory(name=directory_name)
                    root_dir = directory
                else:
                    directory = create_dir_ref(current_dir, directory_name)
                current_dir = directory
        elif 'dir' in out:
            directory_name = out[1]
            create_dir_ref(current_dir, directory_name)
        elif out[0].isnumeric():
            file_size = int(out[0])
            current_dir.files.append(file_size)
            current_dir.total_size = sum(current_dir.files)

    adjust_total_sizes(root_dir)

    return root_dir

def process(lines: list):
    root_dir = mount_dir_tree(lines)

    _, total = calc_size_dirs(root_dir)

    return total

def find_smallest(directory: 'Directory', minimum: int, smallest: int = 0):
    for child in directory.child_dirs:
        child, smallest = find_smallest(child, minimum, smallest)
        if child.total_size >= minimum:
            candidate = child.total_size
            if smallest != 0:
                if candidate <= smallest:
                    smallest = candidate
            else:
                smallest = candidate
    return directory, smallest


def process_2(lines: list):
    root_dir = mount_dir_tree(lines)
    free_space = 70000000 - root_dir.total_size
    minimum = 30000000 - free_space

    _, smallest = find_smallest(root_dir, minimum)

    return smallest


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        result = process_2(lines)
        print(result)


if __name__ == '__main__':
    main()
