from collections import defaultdict

import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    grid = {}
    for x, row in enumerate(input):
        for y, col in enumerate(row):
            grid[(x, y)] = int(col)

    #print(grid)

    visible = set()

    # top_edge = [grid[(0, y)] for y in range(len(input[0]))]

    # bottom_edge = [grid[(len(input)-1, y)] for y in range(len(input[0]))]

    # print(top_edge)
    # print(bottom_edge)

    # left_edge = [grid[(x, 0)] for x in range(len(input))]
    # right_edge = left_edge = [grid[(x, len(input[0])-1)] for x in range(len(input))]

    # print(left_edge)
    # print(right_edge)

    # going down
    tallest = [-1] * len(input[0])
    for x in range(len(input)):
        r = [grid[(x, y)] for y in range(len(input[0]))]
        for y, tree in enumerate(r):
            if tree > tallest[y]:
                visible.add((x, y))
                tallest[y] = tree
            print(tallest, visible)

    # going up
    tallest = [-1] * len(input[0])
    for x in reversed(range(len(input))):
        r = [grid[(x, y)] for y in range(len(input[0]))]
        for y, tree in enumerate(r):
            if tree > tallest[y]:
                visible.add((x, y))
                tallest[y] = tree
            print(tallest, visible)

    tallest = [-1] * len(input)
    for y in range(len(input[0])):
        r = [grid[(x, y)] for x in range(len(input))]
        for x, tree in enumerate(r):
            if tree > tallest[x]:
                visible.add((x, y))
                tallest[x] = tree
        print(r, tallest, visible)


    tallest = [-1] * len(input)
    for y in reversed(range(len(input[0]))):
        r = [grid[(x, y)] for x in range(len(input))]
        for x, tree in enumerate(r):
            if tree > tallest[x]:
                visible.add((x, y))
                tallest[x] = tree
        print(r, tallest, visible)

    return len(visible)


def b_solver(input):
    pass


@advent.command()
def test():
    test_input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390'

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
