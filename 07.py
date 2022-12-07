from collections import defaultdict

import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def parse_input(input):
    current_dir = ""
    total_dirs = defaultdict(int)

    for i in input:
        if '$ cd' in i:
            _, _, path = i.split()
            if path == '/':
                current_dir = '/'
            elif path == '..':
                current_dir = '/'.join(current_dir.split('/')[:-2]) + '/'
            else:
                current_dir = current_dir + path + '/'
        elif i == '$ ls':
            pass
        elif 'dir ' in i:
            pass
        else:
            dirs = current_dir.split('/')[:-1]
            for r in range(len(dirs)):
                total_dirs['/'.join(dirs[:r+1]) + '/'] += int(i.split()[0])

    return total_dirs


def a_solver(input):
    total_dirs = parse_input(input)
    return sum([size for d, size in total_dirs.items() if size < 100000])


def b_solver(input):
    total_dirs = parse_input(input)
    required_size = 30000000 - (70000000 - total_dirs['/'])
    return min([size for d, size in total_dirs.items() if size > required_size])



@advent.command()
def test():
    test_input = [
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
    print("A result:", a_solver(test_input))
    print("B result:", b_solver(test_input))


@advent.command()
def solve():
    print("A result:", a_solver(lines))
    print("B result:", b_solver(lines))


@advent.command()
def submit():
    aocd_submit(a_solver(lines), part="a")
    aocd_submit(b_solver(lines), part="b")


if __name__ == "__main__":
    advent()
