
from dataclasses import dataclass


@dataclass
class Bag:
    color: str
    count: int = 1


def parse_rules(line: str) -> dict:
    # extract the part of sentence containing allowed bags
    ss = line.partition("contain ")[2]
    # split on the word `bag`, handling plural and
    # disacrding end of sentence
    rules = [s.replace("s, ", "").replace(", ", "") for s in ss.split(" bag")[:-1]]
    bag_counts = []
    for rule in rules:
        r = rule.split()
        if r[0] == "no":
            continue
        count = int(r[0])
        name = " ".join(r[1:])
        bag_counts.append(Bag(name, count))
    return bag_counts


def find_containers(rules: dict[str, list[Bag]], bag_color: str) -> list[Bag]:
    result = []
    for color, bags in rules.items():
        for bag in bags:
            if bag.color == bag_color:
                result.append(color)
                break
    return result


def count_bags_containing(bag_color):
    visited = set()
    queue = []

    queue.append(bag_color)
    while len(queue) > 0:
        next_bag = queue.pop()
        if next_bag not in visited:
            for container in find_containers(bag_rules, next_bag):
                queue.append(container)
        
        visited.add(next_bag)

    return len(visited) - 1


def count_bags_inside(bag_color):
    result = 0
    for bag in bag_rules[bag_color]:
        result += bag.count + bag.count * count_bags_inside(bag.color)
    return result


bag_rules = {}
with open('input.txt') as f:
    for line in f.readlines():
        bag_color = " ".join(line.split()[:2])
        bag_rule = parse_rules(line)
        bag_rules[bag_color] = bag_rule


def part1():
    return count_bags_containing("shiny gold")

def part2():
    return count_bags_inside("shiny gold")

print("Part 1:", part1())
print("Part 2:", part2())