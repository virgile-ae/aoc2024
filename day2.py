from itertools import pairwise, combinations
from typing import Iterable


def parse(data: str) -> list[list[int]]:
    return [
        [int(num) for num in nums]
        for line in data.splitlines()
        if (nums := line.split())
    ]


def is_safe(report: Iterable[int]) -> bool:
    differences = [left - right for (left, right) in pairwise(report)]
    between_1_and_3 = all(3 >= abs(difference) >= 1 for difference in differences)
    all_positive = all(difference > 0 for difference in differences)
    all_negative = all(difference < 0 for difference in differences)
    return between_1_and_3 and (all_negative or all_positive)


def part1(data: str) -> int:
    reports = parse(data)
    return len([report for report in reports if is_safe(report)])


def part2(data: str) -> int:
    reports = parse(data)
    return len(
        [
            report
            for report in reports
            if any(
                is_safe(combination)
                for combination in combinations(report, len(report) - 1)
            )
        ]
    )


if __name__ == "__main__":
    from run import run

    data = open("data/day2.txt").read()

    run(part1, data)
    run(part2, data)
