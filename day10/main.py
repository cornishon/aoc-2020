from itertools import groupby
from math import prod, factorial

def differences(l: list[int]) -> list[int]:
    return [i - j for i, j in zip(l[1:], l[:-1]) ]

def binom(n: int, k: int) -> int:
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n-k))
    
def count_combinations(n: int) -> int:
    return sum(binom(n, k) for k in range(3))

def count_ways(l: list[int]) -> int:
    clusters = []
    for k, g in groupby(l):
        if k == 1:
            clusters.append(count_combinations(len(list(g))-1))
    return prod(filter(lambda x: x>0, clusters))

def part1(l: list[int]) -> int:
    diffs = differences(l)
    return diffs.count(1) * diffs.count(3)

def part2(l: list[int]) -> int:
    diffs = differences(l)
    return count_ways(diffs)

def main():
    with open('input.txt') as f:
        adapters = sorted([int(x) for x in f.readlines()] + [0])
        adapters.append(adapters[-1] + 3)
    print("Part 1:", part1(adapters))
    print("Part 2:", part2(adapters))


if __name__ == "__main__":
    main()