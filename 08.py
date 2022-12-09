from collections import defaultdict
import math
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

    visible = set()

    # going down
    tallest = [-1] * len(input[0])
    for x in range(len(input)):
        r = [grid[(x, y)] for y in range(len(input[0]))]
        for y, tree in enumerate(r):
            if tree > tallest[y]:
                visible.add((x, y))
                tallest[y] = tree

    # going up
    tallest = [-1] * len(input[0])
    for x in reversed(range(len(input))):
        r = [grid[(x, y)] for y in range(len(input[0]))]
        for y, tree in enumerate(r):
            if tree > tallest[y]:
                visible.add((x, y))
                tallest[y] = tree

    # going right
    tallest = [-1] * len(input)
    for y in range(len(input[0])):
        r = [grid[(x, y)] for x in range(len(input))]
        for x, tree in enumerate(r):
            if tree > tallest[x]:
                visible.add((x, y))
                tallest[x] = tree

    # going left
    tallest = [-1] * len(input)
    for y in reversed(range(len(input[0]))):
        r = [grid[(x, y)] for x in range(len(input))]
        for x, tree in enumerate(r):
            if tree > tallest[x]:
                visible.add((x, y))
                tallest[x] = tree

    return len(visible)


def b_solver(input):
    grid = {}
    for y, row in enumerate(input):
        for x, col in enumerate(row):
            grid[(x, y)] = int(col)

    scenics = []

    for tree, height in grid.items():
        scenic = [0] * 4
        x, y = tree

        # right
        for mx in range(x+1, len(input[0])):
            scenic[0] += 1
            if grid[(mx, y)] >= height:
                break

        # left
        for mx in range(x-1, -1, -1):
            scenic[1] += 1
            if grid[(mx, y)] >= height:
                break

        # down
        for my in range(y+1, len(input)):
            scenic[2] += 1
            if grid[(x, my)] >= height:
                break

        # left
        for my in range(y-1, -1, -1):
            scenic[3] += 1
            if grid[(x, my)] >= height:
                break

        scenics.append(math.prod(scenic))

    return max(scenics)


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

