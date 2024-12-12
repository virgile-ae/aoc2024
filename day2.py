from itertools import pairwise, combinations
from typing import Iterable


def is_safe(report: Iterable[int]) -> bool:
    differences = [left - right for (left, right) in pairwise(report)]
    between_1_and_3 = all(3 >= abs(difference) >= 1 for difference in differences)
    all_positive = all(difference > 0 for difference in differences)
    all_negative = all(difference < 0 for difference in differences)
    return between_1_and_3 and (all_negative or all_positive)


def part1(reports: list[list[int]]) -> int:
    return len([report for report in reports if is_safe(report)])


def part2(reports: list[list[int]]) -> int:
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
    data = open("data/day2.txt").read()

    reports = [
        [int(num) for num in nums]
        for line in data.splitlines()
        if (nums := line.split())
    ]

    result1 = part1(reports)
    result2 = part2(reports)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
