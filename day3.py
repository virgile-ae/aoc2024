import re

MUL_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
DO_PATTERN = re.compile(r"do\(\)")
DONT_PATTERN = re.compile(r"don't\(\)")


def part1(data: str) -> int:
    multiplications = MUL_PATTERN.findall(data)
    return sum(int(left) * int(right) for (left, right) in multiplications)


def part2(data: str) -> int:
    enable_mul = True
    accumulator = 0
    for i in range(len(data)):
        if DO_PATTERN.match(data[i:]):
            enable_mul = True
        elif DONT_PATTERN.match(data[i:]):
            enable_mul = False
        elif enable_mul and (matched := MUL_PATTERN.match(data[i:])):
            (left, right) = matched.group(1, 2)
            accumulator += int(left) * int(right)

    return accumulator


if __name__ == "__main__":
    data = None

    data = open("data/day3.txt").read()

    result1 = part1(data)
    result2 = part2(data)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")