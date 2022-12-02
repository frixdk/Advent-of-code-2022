
import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    score = {
        ('A', 'X'): 3 + 1,
        ('A', 'Y'): 6 + 2,
        ('A', 'Z'): 0 + 3,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 6 + 1,
        ('C', 'Y'): 0 + 2,
        ('C', 'Z'): 3 + 3
    }

    total = 0

    for i in input:
        o, p = i.split()
        total += score[(o, p)]

    return total


def b_solver(input):
    score = {
        ('A', 'X'): 0 + 3,
        ('A', 'Y'): 3 + 1,
        ('A', 'Z'): 6 + 2,
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        ('C', 'X'): 0 + 2,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 6 + 1
    }

    total = 0

    for i in input:
        o, p = i.split()
        total += score[(o, p)]

    return total

@advent.command()
def test():
    test_input = [
        'A Y',
        'B X',
        'C Z'
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
