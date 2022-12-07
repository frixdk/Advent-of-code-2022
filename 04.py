import click
from aocd import data, lines, numbers
from aocd import submit as aocd_submit

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.1")
def advent():
    pass


def a_solver(input):
    contained = 0
    for i in input:
        a, b, c, d = *i.split(",")[0].split("-"), *i.split(",")[1].split("-")

        if (not set(range(int(a), int(b) + 1)) - set(range(int(c), int(d) + 1)) or
        not set(range(int(c), int(d) + 1)) - set(range(int(a), int(b) + 1))):
            contained += 1

    return contained


def b_solver(input):
    overlap = 0
    for i in input:
        a, b, c, d = *i.split(",")[0].split("-"), *i.split(",")[1].split("-")

        if set(range(int(a), int(b) + 1)) & set(range(int(c), int(d) + 1)):
            overlap += 1

    return overlap


@advent.command()
def test():
    test_input = [
        "2 - 4, 6 - 8",
        "2 - 3, 4 - 5",
        "5 - 7, 7 - 9",
        "2 - 8, 3 - 7",
        "6 - 6, 4 - 6",
        "2 - 6, 4 - 8"
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
