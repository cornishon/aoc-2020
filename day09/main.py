SAMPLE = False

def is_sum(index: int, numbers: list[int], preamble_len: int) -> bool:
    preamble = numbers[index - preamble_len:index]
    n = numbers[index]
    for i, p1 in enumerate(preamble):
        for p2 in preamble[i:]:
            if p1 + p2 == n:
                return True
    return False

def find_sequence(
    invalid_number: int, numbers: list[int]
    ) -> tuple[int, int]:
    for i, _ in enumerate(numbers):
        start = i
        end = i
        total = 0
        while total < invalid_number:
            total += numbers[i]
            i += 1
            end += 1
        if total == invalid_number:
            return numbers[start:end]

def part1(numbers: list[int], preamble_len: int) -> int:
    for i in range(preamble_len, len(numbers)):
        if not is_sum(i, numbers, preamble_len):
            return numbers[i]

def part2(invalid_number: int, numbers: list[int]) -> int:
    sequence = find_sequence(invalid_number, numbers)
    return min(sequence) + max(sequence)


def main():
    if SAMPLE:
        filename = "sample.txt"
        preamble_len = 5
    else:
        filename = "input.txt"
        preamble_len = 25

    with open(filename) as f:
        numbers = [int(n) for n in f.readlines()]

    invalid_number = part1(numbers, preamble_len)
    print("Part 1:", invalid_number)
    print("Part 2:", part2(invalid_number, numbers))

if __name__ == "__main__":
    main()