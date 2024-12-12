from typing import Iterable, Self


class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(f"{self.x},{self.y}")

    def __iter__(self) -> Iterable[int]:
        return iter((self.x, self.y))

    def __mul__(self, other: "int | Vector") -> "Vector | int":
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __sub__(self, other: Self) -> "Vector":
        return self + (-other)


UP = Vector(0, -1)
DOWN = Vector(0, 1)
LEFT = Vector(-1, 0)
RIGHT = Vector(1, 0)

ROTATE_CLOCKWISE = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
}


def parse(data: str) -> tuple[list[list[bool]], Vector]:
    grid = [[char == "#" for char in line] for line in data.splitlines()]

    grid_width = len(grid[0]) + 1
    guard_index = data.index("^")
    guard_position = Vector(guard_index % grid_width, guard_index // grid_width)

    return (grid, guard_position)


def within_grid(grid: list[list[bool]], guard_position: Vector) -> bool:
    GRID_WIDTH = len(grid[0])
    GRID_HEIGHT = len(grid)
    return 0 <= guard_position.x < GRID_WIDTH and 0 <= guard_position.y < GRID_HEIGHT


def is_obstructed(grid: list[list[bool]], coord: Vector) -> bool:
    return within_grid(grid, coord) and grid[coord.y][coord.x]


def print_grid(grid: list[list[bool]], *positions: Vector) -> None:
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if Vector(x, y) in positions:
                print(".", end="")
            else:
                print("#" if char else " ", end="")
        print()


def part1(data: str) -> int:
    grid, guard_position = parse(data)
    positions: set[Vector] = set()
    guard_direction = UP

    while within_grid(grid, guard_position):
        positions.add(guard_position)
        new_position = guard_position + guard_direction
        if is_obstructed(grid, new_position):
            guard_direction = ROTATE_CLOCKWISE[guard_direction]
        else:
            guard_position = new_position

    print_grid(grid, *positions)

    return len(positions)


def is_loop(grid: list[list[bool]], square: Vector, guard_position: Vector) -> bool:
    if grid[square.y][square.x]:
        return False

    positions: set[tuple[Vector, Vector]] = set()
    guard_direction = UP
    grid[square.y][square.x] = True

    while (
        within_grid(grid, guard_position)
        and (guard_position, guard_direction) not in positions
    ):
        positions.add((guard_position, guard_direction))
        new_position = guard_position + guard_direction
        if is_obstructed(grid, new_position):
            guard_direction = ROTATE_CLOCKWISE[guard_direction]
        else:
            guard_position = new_position

    res = (guard_position, guard_direction) in positions
    grid[square.y][square.x] = False

    return res


def part2(data: str) -> int:
    grid, guard_position = parse(data)

    grid_width = len(grid[0])
    grid_height = len(grid)

    return sum(
        1 if is_loop(grid, Vector(x, y), guard_position) else 0
        for x in range(grid_width)
        for y in range(grid_height)
    )


if __name__ == "__main__":
    from run import run
    from testing import test

    test_data = open("data/test6.txt").read()
    data = open("data/day6.txt").read()

    test(part1, data=test_data, expected=41)
    test(part2, data=test_data, expected=6)

    run(part1, data)
    run(part2, data)
