Room = list[list[str]]
Pair = tuple[int, int]

def pad(room: Room) -> Room:
    new_room = []
    n = len(room[0])
    new_room.append((n+2) * ['.'])
    for row in room:
        new_room.append(['.'] + row + ['.'])
    new_room.append((n+2) * ['.'])
    return new_room

def neighbors(loc: Pair) -> list[Pair]:
    i, j = loc
    return [(x, y) for x in [i-1, i, i+1] for y in [j-1, j, j+1]
        if not (x == i and y == j)]

def neighborhood(loc: Pair, room: Room) -> list[str]:
    result = []
    for x, y in neighbors(loc):
        result.append(room[x][y])
    return result

DIRS = {
    'NE': (1, 1),
    'E': (0, 1),
    'SE': (-1, 1),
    'S': (-1, 0),
    'SW': (-1, -1),
    'W': (0, -1),
    'NW': (1, -1),
    'N': (1, 0),
}


def closest_visible(loc: Pair, room: Room, direction: Pair) -> str:
    xbounds = range(0, len(room[0]) - 1)
    ybounds = range(0, len(room) - 1)
    y, x = loc
    dy, dx = direction
    y = y + dy
    x = x + dx
    cell = room[y][x] 
    if cell == '#' or cell == 'L':
        return cell
    else:
        if (x not in xbounds) or (y not in ybounds):
            return '.'
        else:
            return closest_visible((y, x), room, direction)
        

def advance2(room: Room) -> Room:
    n = len(room)
    m = len(room[0])
    new_room = [m * ['.'] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if room[i][j] == '.':
                new_room[i][j] = '.'
                continue
            seen = []
            for direction in DIRS.values():
                seen.append(closest_visible((i,j), room, direction))

            cnt = seen.count('#')
            if room[i][j] == 'L':
                if cnt == 0:
                    new_room[i][j] = '#'
                else:
                    new_room[i][j] = 'L'
            else:
                if cnt >= 5:
                    new_room[i][j] = 'L'
                else:
                    new_room[i][j] = '#'
                    
    return new_room

def advance(room: Room) -> Room:
    n = len(room)
    m = len(room[0])
    new_room = [m * ['.'] for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if room[i][j] == '.':
                new_room[i][j] = '.'
                continue
            else:
                cnt = neighborhood((i,j), room).count('#')

            if room[i][j] == 'L':
                if cnt == 0:
                    new_room[i][j] = '#'
                else:
                    new_room[i][j] = 'L'
            else:
                if cnt >= 4:
                    new_room[i][j] = 'L'
                else:
                    new_room[i][j] = '#'
    return new_room

def simulate(room: Room, advancer: callable) -> Room:
    current = room
    new_room = advancer(current)
    while new_room != current:
        current = new_room
        new_room = advancer(current)
    return new_room

def part1(initial: Room) -> int:
    final = simulate(initial, advance)
    return sum([row.count('#') for row in final])


def part2(initial: Room) -> int:
    final = simulate(initial, advance2)
    return sum([row.count('#') for row in final])    


def main():
    with open("input.txt") as f:
        seats = []
        for line in f.readlines():
            seats.append([c for c in line.strip()])

    initial = pad(seats)
    print("Part 1:", part1(initial))
    print("Part 2:", part2(initial))
        

if __name__ == "__main__":
    main()