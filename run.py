from typing import Callable


def run(solution: Callable[[str], int], data: str) -> None:
    result1 = solution(data)
    is_part1 = solution.__name__ == "part1"
    part = 1 if is_part1 else 2
    print(f"Part {part}: {result1}")
