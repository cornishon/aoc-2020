mins = []
maxes = []
chars = []
passwords = []

def parse_line(line):
    l = line.split()
    if len(l) == 3:
        passwords.append(l[-1])
        chars.append(l[-2].strip(":"))
        bounds = l[0].split("-")
        mins.append(int(bounds[0]))
        maxes.append(int(bounds[1]))


with open("input.txt") as f:
    for line in f:
        parse_line(line)


def part1():
    valid_count = 0
    for lb, ub, ch, p in zip(mins, maxes, chars, passwords):
       cnt = p.count(ch)
       if lb <= cnt <= ub:
           valid_count += 1
    return valid_count


def part2():
    valid_count = 0
    for lb, ub, ch, p in zip(mins, maxes, chars, passwords):
        if p[lb-1] == ch and p[ub-1] != ch:
            valid_count +=1
        elif p[lb-1] != ch and p[ub-1] == ch:
            valid_count += 1
    return valid_count


print("Part 1:", part1())
print("Part 2:", part2())

