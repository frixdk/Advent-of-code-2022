import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    msg = input[0]
    for r in range(len(msg)):
        if len(set(msg[r:r+4])) == 4:
            return r+4


def b_solver(input):
    msg = input[0]
    for r in range(len(msg)):
        if len(set(msg[r:r+14])) == 14:
            return r+14


@advent.command()
def test():
    test_input = [
        'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
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
