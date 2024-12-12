from itertools import product
from operator import add, mul
from typing import Iterator, Callable, Any


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def parse(data: str) -> Iterator[tuple[int, list[int]]]:
    for line in data.splitlines():
        [lhs, elements] = line.split(": ")
        yield (int(lhs), [int(element) for element in elements.split()])


def apply(operators: tuple[Callable[[Any, Any], Any], ...], elements: list[int]) -> int:
    acc: int = elements[0]
    for operator, element in zip(operators, elements[1:]):
        acc = operator(acc, element)
    return acc


def can_make(
    num: int, using: list[int], by_combining: list[Callable[[Any, Any], Any]]
) -> bool:
    operators = by_combining
    elements = using
    operator_combinations = list(product(operators, repeat=len(elements) - 1))
    return any(
        [apply(operators, elements) == num for operators in operator_combinations]
    )


def part1(data: str) -> int:
    equations = parse(data)
    return sum(
        result
        for (result, elements) in equations
        if can_make(result, using=elements, by_combining=[add, mul])
    )


def part2(data: str) -> int:
    equations = parse(data)
    return sum(
        result
        for (result, elements) in equations
        if can_make(result, using=elements, by_combining=[add, mul, concat])
    )


if __name__ == "__main__":
    from run import run
    from testing import test

    test_data = open("data/test7.txt").read()
    data = open("data/day7.txt").read()

    test(part1, data=test_data, expected=3749)
    test(part2, data=test_data, expected=11387)

    run(part1, data)
    run(part2, data)
