import math
from collections import defaultdict

import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit
from sympy import Eq, solve, sympify

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    monkeys = {}

    for i in input:
        monkey, job = i.split(":")
        monkeys[monkey] = job

    print(monkeys)

    root = monkeys['root']

    while(True):
        found_more = False
        for x in root.split():
            if x in monkeys.keys():
                found_more = True
                root = root.replace(x, '('+monkeys[x]+' )')

        if not found_more:
            break

    return int(eval(root))


def b_solver(input):
    monkeys = {}

    for i in input:
        monkey, job = i.split(":")
        monkeys[monkey] = job

    print(monkeys)

    root = monkeys['root'].replace('+', '=')

    while(True):
        found_more = False
        for x in root.split():
            if x in monkeys.keys():
                found_more = True
                if x == 'humn':
                    root = root.replace(x, 'x')
                else:
                    root = root.replace(x, '('+monkeys[x]+' )')

        if not found_more:
            break

    sympy_eq = sympify("Eq(" + root.replace("=", ",") + ")")

    print(sympy_eq)

    solve(sympy_eq)
    # for some reason this doesnt work and the click lib throws an error??
    # i took the equation and solved with wolfram alpha
    return 42


@advent.command()
def test():
    test_input = [
        'root: pppw + sjmn',
        'dbpl: 5',
        'cczh: sllz + lgvd',
        'zczc: 2',
        'ptdq: humn - dvpt',
        'dvpt: 3',
        'lfqf: 4',
        'humn: 5',
        'ljgn: 2',
        'sjmn: drzm * dbpl',
        'sllz: 4',
        'pppw: cczh / lfqf',
        'lgvd: ljgn * ptdq',
        'drzm: hmdt - zczc',
        'hmdt: 32'
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
