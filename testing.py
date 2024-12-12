from typing import Callable


def test[S, T](f: Callable[[S], T], data: S, expected: T) -> None:
    is_part1 = f.__name__ == "part1"
    part = 1 if is_part1 else 2
    result = f(data)
    if result == expected:
        print(f"[✓] Test {part} passed")
    else:
        print(f"[✗] Test {part} failed, got '{result}' but expected '{expected}'")
