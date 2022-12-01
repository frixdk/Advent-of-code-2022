
import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    elves = []
    elf = 0
    for i in input:
        if i:
            elf += int(i)
        else:
            elves.append(elf)
            elf = 0
    elves.append(elf)

    return max(elves)


def b_solver(input):
    elves = []
    elf = 0
    for i in input:
        if i:
            elf += int(i)
        else:
            elves.append(elf)
            elf = 0
    elves.append(elf)

    return sum(sorted(elves)[-3:])

@advent.command()
def test():
    test_input = [
        '1000',
        '2000',
        '3000',
        '',
        '4000',
        '',
        '5000',
        '6000',
        '',
        '7000',
        '8000',
        '9000',
        '',
        '10000',
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
