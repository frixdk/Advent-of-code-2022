import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    priorites = []
    for i in input:
        a, b = i[:int(len(i)/2)], i[int(len(i)/2):]
        shared = ord([c for c in a if c in b][0])-96
        if shared < 1:
            shared = shared + 58
        priorites.append(shared)

    return sum(priorites)


def b_solver(input):
    priorites = []
    for r in range(0, len(input), 3):
        shared = ord([c for c in input[r] if c in input[r+1] and c in input[r+2]][0]) - 96

        if shared < 1:
            shared = shared + 58

        priorites.append(shared)

    return sum(priorites)

@advent.command()
def test():
    test_input = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
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
