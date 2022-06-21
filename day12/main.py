from enum import Enum

Program = list[tuple[str, int]]

class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Ship():
    def __init__(self, x=0, y=0, facing=Dir.E):
        self.x = x
        self.y = y
        self.facing = facing
        self.waypoint_x = 10
        self.waypoint_y = 1

    def __repr__(self) -> str:
        return f"{self.x}, {self.y}, {self.facing}"
    
    @property
    def distance(self) -> int:
        return abs(self.x) + abs(self.y)
    
    def move(self, dir: Dir, ammount: int) -> None:
        dy, dx = DIRS[dir.value]
        self.x += dx * ammount
        self.y += dy * ammount
    
    def move_waypoint(self, dir: Dir, ammount: int) -> None:
        dy, dx = DIRS[dir.value]
        self.waypoint_x += dx * ammount
        self.waypoint_y += dy * ammount
    
    def move_toward_waypoint(self, ammount: int) -> None:
        self.x += self.waypoint_x * ammount
        self.y += self.waypoint_y * ammount

    def _rot90(self):
        new_x = self.waypoint_y
        new_y = -self.waypoint_x
        self.waypoint_x = new_x
        self.waypoint_y = new_y

    def rotate_waypoint(self, angle: int) -> None:
        times = (angle // 90) % 4
        for _ in range(times):
            self._rot90()
    
    def forward(self, ammount: int) -> None:
        self.move(self.facing, ammount)    

    def turn(self, angle: int) -> None:
        rotations = angle // 90
        old = self.facing.value
        dir = (old + rotations) % 4
        self.facing = Dir(dir)


def simulate_v1(ship: Ship, program: Program) -> None:
    for op, arg in program:
        if op == 'N':
            ship.move(Dir.N, arg)
        elif op == 'E':
            ship.move(Dir.E, arg)
        elif op == 'S':
            ship.move(Dir.S, arg)
        elif op == 'W':
            ship.move(Dir.W, arg)
        elif op == 'F':
            ship.forward(arg)
        elif op == 'R':
            ship.turn(arg)
        elif op == 'L':
            ship.turn(-arg)
        else:
            print("unreachable")

def simulate_v2(ship: Ship, program: Program) -> None:
    for op, arg in program:
        if op == 'N':
            ship.move_waypoint(Dir.N, arg)
        elif op == 'E':
            ship.move_waypoint(Dir.E, arg)
        elif op == 'S':
            ship.move_waypoint(Dir.S, arg)
        elif op == 'W':
            ship.move_waypoint(Dir.W, arg)
        elif op == 'F':
            ship.move_toward_waypoint(arg)
        elif op == 'R':
            ship.rotate_waypoint(arg)
        elif op == 'L':
            ship.rotate_waypoint(-arg)
        else:
            print("unreachable")

def part1(ship: Ship, program: Program) -> int:
    simulate_v1(ship, program)
    return ship.distance

def part2(ship: Ship, program: Program) -> int:
    simulate_v2(ship, program)
    return ship.distance

def main():
    with open('input.txt') as f:
        instructions = []
        for line in f.readlines():
            l = line.strip()
            action = l[0]
            arg = int(l[1:])
            instructions.append((action, arg))
    
    print("Part 1:", part1(Ship(), instructions))
    print("Part 2:", part2(Ship(), instructions))


if __name__ == "__main__":
    main()
