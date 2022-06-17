def seat_id(line: str) -> int:
    row = int(line[:-3].replace("F","0").replace("B","1"), base=2)
    col = int(line[-3:].replace("L","0").replace("R","1"), base=2)
    return 8*row + col

with open('input.txt') as f:
    ids = []
    for line in f.readlines():
        ids.append(seat_id(line.strip()))


def part1():
    return max(ids)

def part2():
    return (set(range(min(ids), max(ids)+1)) - set(ids)).pop()


print("Part 1:", part1())

print("Part 2:", part2())