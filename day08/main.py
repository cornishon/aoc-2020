from dataclasses import dataclass


@dataclass(slots=True)
class Operation:
    op: str
    arg: int

Program = list[Operation]


class Machine:
    def __init__(self, ops: Program) -> None:
        self.ip = 0
        self.acc = 0
        self.ops = ops
    
    @property
    def max_ip(self) -> int:
        return len(self.ops) - 1

    def advance(self) -> None:
        oper = self.ops[self.ip]
        if oper.op == "nop":
            self.ip += 1
        elif oper.op == "acc":
            self.acc += oper.arg
            self.ip += 1
        elif oper.op == "jmp":
            self.ip += oper.arg
        else:
            return ValueError()

    def run_until_repeat(self) -> tuple[int, bool]:
        visited_ips = []
        while self.ip not in visited_ips:
            visited_ips.append(self.ip)
            self.advance()
            if self.ip > self.max_ip:
                return self.acc, True
        return self.acc, False


def bugfix(ops: Program) -> int:
    for i, op in enumerate(ops):
        if op.op == "acc":
            continue
        elif op.op == "jmp":
            new_ops = ops.copy()
            new_ops[i] = Operation("nop", new_ops[i].arg)
        else:
            new_ops = ops.copy()
            new_ops[i] = Operation("jmp", new_ops[i].arg)

        m = Machine(new_ops)
        acc, terminated = m.run_until_repeat()
        if terminated:
            return acc


def main():
    ops = []
    with open("input.txt") as f:
        for line in f.readlines():
            op, arg = line.split()
            ops.append(Operation(op, int(arg)))

    m = Machine(ops)
    print("Part 1:", m.run_until_repeat()[0])

    print("Part 2:", bugfix(ops))


if __name__ == "__main__":
    main()