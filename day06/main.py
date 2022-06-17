with open('input.txt') as f:
    groups = f.read().split('\n\n')

def counts_any(groups: list[str]) -> list[int]:
    counts = []
    for group in groups:
        counts.append(len(set(group.replace('\n', ''))))
    return counts

def counts_all(groups: list[str]) -> list[int]:
    counts = []
    for group in groups:
        individuals = [set(x) for x in group.split()]
        counts.append(len(set.intersection(*individuals)))
    return counts

def part1():
    return sum(counts_any(groups))

def part2():
    return sum(counts_all(groups))

print("Part 1:", part1())
print("Part 2:", part2())

# print(counts)