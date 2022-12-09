import unittest

from main import process, process_2, find_directory, create_dir_ref, Directory

class TestMain(unittest.TestCase):
    test = [
        '$ cd /',
        '$ ls',
        'dir a',
        '14848514 b.txt',
        '8504156 c.dat',
        'dir d',
        '$ cd a',
        '$ ls',
        'dir e',
        '29116 f',
        '2557 g',
        '62596 h.lst',
        '$ cd e',
        '$ ls',
        '584 i',
        '$ cd ..',
        '$ cd ..',
        '$ cd d',
        '$ ls',
        '4060174 j',
        '8033020 d.log',
        '5626152 d.ext',
        '7214296 k'
    ]

    def test_process(self):
        result = process(self.test)

        self.assertEqual(result, 95437, 'Should be 95437')

    def test_find_directory(self):
        dir_root = Directory(name='/')

        dir_a = Directory(parent_dir=dir_root, name='a')
        dir_b = Directory(parent_dir=dir_root, name='b')
        dir_root.child_dirs = [dir_a, dir_b]

        dir_c = Directory(parent_dir=dir_a, name='c')
        dir_a.child_dirs = [dir_c]

        # Find B
        result = find_directory(dir_root, name='b')

        assert result == dir_b

        # Find C
        result = find_directory(dir_a, name='c')

        assert result == dir_c

    def test_create_dir_ref(self):
        # Without created
        dir_root = Directory(name='/')
        result = create_dir_ref(dir_root, 'a')

        assert result.name == 'a'
        assert result.parent_dir == dir_root

        # With created
        dir_root = Directory(name='/')
        dir_b = Directory(name='b', parent_dir=dir_root)
        dir_root.child_dirs.append(dir_b)
        result = create_dir_ref(dir_root, 'b')

        assert result.name == 'b'
        assert result.parent_dir == dir_root

    def test_process_2(self):
        result = process_2(self.test)

        self.assertEqual(result, 24933642, 'Should be 24933642')

if __name__ == '__main__':
    unittest.main()
