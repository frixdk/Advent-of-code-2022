import math
from collections import defaultdict

import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def draw(head, tail):
    board = []
    for y in range(5):
        row = []
        for x in range(6):
            if [x, y] == head:
                row.append("H")
            elif [x, y] == tail:
                row.append("T")
            elif [x, y] == [0, 0]:
                row.append("s")
            else:
                row.append(".")
        board.append(row)

    for row in reversed(board):
        print("".join(row))

    print()


def a_solver(input):
    head = [0, 0]
    tail = [0, 0]

    draw(head, tail)

    visits = set()

    for i in input:

        print("==", i, "==")
        print()

        direction, steps = i.split()
        for _ in range(int(steps)):

            if direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            elif direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1

            diff = tail[0] - head[0], tail[1] - head[1]
            dist = math.sqrt(abs(diff[0]) ** 2 + abs(diff[1]) ** 2)

            if dist > 1.5:
                diff = [int(c/abs(c)) if c != 0 else c for c in diff]
                # snapping to behind head
                if direction in ['U', 'D']:
                    tail = [head[0], head[1] + diff[1]]
                elif direction in ['R', 'L']:
                    tail = [head[0] + diff[0], head[1]]

            visits.add((tail[0], tail[1]))
            draw(head, tail)

    print(visits)
    return len(visits)

def draw_rope(head, tails):
    board = []
    for y in range(-10, 16):
        row = []
        for x in range(-14, 14):
            if [x, y] == head:
                row.append("H")
            elif [x, y] in tails:
                row.append(str(tails.index([x, y])+1))
            elif [x, y] == [0, 0]:
                row.append("s")
            else:
                row.append(".")
        board.append(row)

    for row in reversed(board):
        print("".join(row))

    print()


def move_tail(head, tail):
    diff = tail[0] - head[0], tail[1] - head[1]

    if abs(diff[0]) > 1 and abs(diff[1]) > 1:
        # diagonalos
        tail[0] = head[0] + int(diff[0]/abs(diff[0]))
        tail[1] = head[1] + int(diff[1]/abs(diff[1]))
    elif abs(diff[0]) > 1:
        tail[0] = head[0] + int(diff[0]/abs(diff[0]))
        tail[1] = head[1]
    elif abs(diff[1]) > 1:
        tail[1] = head[1] + int(diff[1]/abs(diff[1]))
        tail[0] = head[0]

    return tail


def b_solver(input):
    head = [0, 0]
    tails = [[0, 0] for _ in range(9)]

    print(tails)

    draw_rope(head, tails)

    visits = set()

    for i in input:

        print("==", i, "==")
        print()

        direction, steps = i.split()
        for _ in range(int(steps)):

            if direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            elif direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1

            # move tails
            tails[0] = move_tail(head, tails[0])
            for i in range(1, len(tails)):
                tails[i] = move_tail(tails[i-1], tails[i])

            draw_rope(head, tails)

            visits.add((tails[8][0], tails[8][1]))

    print(visits)
    return len(visits)


@advent.command()
def test():
    test_input = [
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2'
    ]

    test_input_larger = [
        'R 5 ',
        'U 8 ',
        'L 8 ',
        'D 3 ',
        'R 17',
        'D 10',
        'L 25',
        'U 20'
    ]
    print("A result:", a_solver(test_input))
    print("B result:", b_solver(test_input))
    print("B result:", b_solver(test_input_larger))


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
