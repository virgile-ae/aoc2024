from day6 import Vector
from itertools import combinations
from copy import copy


def parse(data: str) -> tuple[dict[str, list[Vector]], int, int]:
    """
    Returns a tuple containing
    - A dictionary with the locations of each antennae indexed by frequency.
    - The width of the map.
    - The height of the map.
    """
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)

    antennae: dict[str, list[Vector]] = dict()

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == ".":
                continue

            position = Vector(x, y)
            if char in antennae:
                antennae[char].append(position)
            else:
                antennae[char] = [position]

    return antennae, width, height


def part1(data: str) -> int:
    # Find all combinations of pairs of antennae for each frequency
    # Find antinodes for each pair
    # Count unique antinodes
    antennae, width, height = parse(data)
    antinodes: set[Vector] = set()

    for positions in antennae.values():
        for a, b in combinations(positions, 2):
            ab = b - a
            antinode1 = a - ab
            antinode2 = b + ab

            if 0 <= antinode1.x < width and 0 <= antinode1.y < height:
                antinodes.add(antinode1)
            if 0 <= antinode2.x < width and 0 <= antinode2.y < height:
                antinodes.add(antinode2)

    return len(antinodes)


def find_antinodes(
    width: int, height: int, antenna_a: Vector, antenna_b: Vector
) -> set[Vector]:
    antinodes: set[Vector] = set()

    ab = antenna_b - antenna_a
    # One direction
    position = copy(antenna_b)
    while 0 <= position.x < width and 0 <= position.y < height:
        antinodes.add(position)
        position += ab

    # Now the other
    position = copy(antenna_a)
    while 0 <= position.x < width and 0 <= position.y < height:
        antinodes.add(position)
        position -= ab

    return antinodes


def part2(data: str) -> int:
    # Sames as for `part1` except now `find_antinodes` is used to find all
    # resonant antinodes.
    antennae, width, height = parse(data)
    antinodes: set[Vector] = set()

    for positions in antennae.values():
        for a, b in combinations(positions, 2):
            antinodes |= find_antinodes(width, height, a, b)

    return len(antinodes)


if __name__ == "__main__":
    from testing import test

    test_data = open("data/test8.txt").read()
    data = open("data/day8.txt").read()

    test(part1, data=test_data, expected=14)
    test(part2, data=test_data, expected=34)

    result1 = part1(data)
    print(f"Part 1: {result1}")
    result2 = part2(data)
    print(f"Part 2: {result2}")
