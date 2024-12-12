from functools import cache


def parse(data: str) -> list[int]:
    return [int(stone) for stone in data.split()]


def transform_stone(stone: int) -> list[int]:
    match stone:
        case 0:
            return [1]
        case x if len(str(x)) % 2 == 0:
            digits = str(x)
            halfway = len(digits) // 2
            return [int(digits[:halfway]), int(digits[halfway:])]
        case _:
            return [stone * 2024]


def blink(stones: list[int]) -> list[int]:
    return [new_stone for stone in stones for new_stone in transform_stone(stone)]


def part1(data: str) -> int:
    stones = parse(data)

    for _ in range(25):
        stones = blink(stones)

    return len(stones)


@cache
def blink_length(stone: int, depth: int = 0) -> int:
    if depth == 75:
        return 1
    new_stones = blink([stone])
    return sum(blink_length(new_stone, depth=depth + 1) for new_stone in new_stones)


def part2(data: str) -> int:
    stones = parse(data)
    return sum(blink_length(stone) for stone in stones)


if __name__ == "__main__":
    from testing import test
    from run import run

    test_data = open("data/test11.txt").read()
    data = open("data/day11.txt").read()

    test(part1, data=test_data, expected=55312)
    run(part1, data)
    run(part2, data)
