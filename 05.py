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
    s = input.index('')

    stack_input = input[:s]
    for si in stack_input:
        print(si)

    stacks = defaultdict(list)

    for index, bot in enumerate(stack_input[-1]):
        if bot.strip():
            for boxes in reversed(input[:s-1]):
                if index < len(boxes) and boxes[index].strip():
                    stacks[int(bot)].append(boxes[index])

    return stacks, input[s+1:]


def a_solver(input):
    stacks, instructions = parse_input(input)

    for i in instructions:
        amount, stack_source, stack_destination = [int(x) for x in [i.split()[1], i.split()[3], i.split()[5]]]
        for _ in range(amount):
            stacks[stack_destination].append(stacks[stack_source].pop())

    return ''.join([stack[-1] for _, stack in stacks.items()])


def b_solver(input):
    stacks, instructions = parse_input(input)

    for i in instructions:
        amount, stack_source, stack_destination = [int(x) for x in [i.split()[1], i.split()[3], i.split()[5]]]

        stacks[stack_destination].extend(stacks[stack_source][-amount:])
        stacks[stack_source] = stacks[stack_source][:-amount]

    return ''.join([stack[-1] for _, stack in stacks.items()])


@advent.command()
def test():
    test_input = [
        '    [D]',
        '[N] [C]',
        '[Z] [M] [P]',
        ' 1   2   3',
        '',
        'move 1 from 2 to 1',
        'move 3 from 1 to 3',
        'move 2 from 2 to 1',
        'move 1 from 1 to 2'

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
