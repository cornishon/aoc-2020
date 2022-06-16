forest_map = []
with open('input.txt') as f:
    for line in f:
        forest_map.append(line.strip())


def count_trees(map: list, dx: int, dy: int) -> int:
    n = len(map[0])
    trees_encountered = 0
    x, y = 0, 0
    while y < len(map):
        if map[y][x % n] == '#':
            trees_encountered += 1
        y += dy
        x += dx
    return trees_encountered

def part1():
    return count_trees(forest_map, 3, 1)


def part2():
    product = 1
    product *= count_trees(forest_map, 1, 1)
    product *= count_trees(forest_map, 3, 1)
    product *= count_trees(forest_map, 5, 1)
    product *= count_trees(forest_map, 7, 1)
    product *= count_trees(forest_map, 1, 2)
    return product


print("Part 1:", part1())
print("Part 2:", part2())