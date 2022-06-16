import itertools

with open("input.txt", "r") as f:
    entries = [int(x.strip()) for x in f.readlines()]

def part1():
    for e1, e2 in itertools.product(entries, repeat=2):
        if e1+e2 == 2020:
            return e1*e2


def part2():
    for e1, e2, e3 in itertools.product(entries, repeat=3):
        if e1+e2+e3 == 2020:
            return e1*e2*e3


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
