def parse(data: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in data.splitlines()]


def trailhead_ends(
    tmap: list[list[int]], x: int, y: int, start_height: int = 0
) -> set[tuple[int, int]]:
    if tmap[y][x] != start_height:
        return set()

    if tmap[y][x] == 9:
        return {(x, y)}

    path_ends: set[tuple[int, int]] = set()

    MAP_WIDTH = len(tmap[0])
    MAP_HEIGHT = len(tmap)

    if 1 <= y and tmap[y - 1][x] == start_height + 1:
        path_ends |= trailhead_ends(tmap, x, y - 1, start_height + 1)
    if y < MAP_WIDTH - 1 and tmap[y + 1][x] == start_height + 1:
        path_ends |= trailhead_ends(tmap, x, y + 1, start_height + 1)
    if 1 <= x and tmap[y][x - 1] == start_height + 1:
        path_ends |= trailhead_ends(tmap, x - 1, y, start_height + 1)
    if x < MAP_HEIGHT - 1 and tmap[y][x + 1] == start_height + 1:
        path_ends |= trailhead_ends(tmap, x + 1, y, start_height + 1)

    return path_ends


def part1(data: str) -> int:
    tmap = parse(data)

    MAP_WIDTH = len(tmap[0])
    MAP_HEIGHT = len(tmap)

    return sum(
        len(trailhead_ends(tmap, x, y))
        for x in range(MAP_WIDTH)
        for y in range(MAP_HEIGHT)
    )


def trailhead_scores(
    tmap: list[list[int]], x: int, y: int, start_height: int = 0
) -> int:
    if tmap[y][x] != start_height:
        return 0

    if tmap[y][x] == 9:
        return 1

    score_sum = 0

    MAP_WIDTH = len(tmap[0])
    MAP_HEIGHT = len(tmap)

    if 1 <= y and tmap[y - 1][x] == start_height + 1:
        score_sum += trailhead_scores(tmap, x, y - 1, start_height + 1)
    if y < MAP_WIDTH - 1 and tmap[y + 1][x] == start_height + 1:
        score_sum += trailhead_scores(tmap, x, y + 1, start_height + 1)
    if 1 <= x and tmap[y][x - 1] == start_height + 1:
        score_sum += trailhead_scores(tmap, x - 1, y, start_height + 1)
    if x < MAP_HEIGHT - 1 and tmap[y][x + 1] == start_height + 1:
        score_sum += trailhead_scores(tmap, x + 1, y, start_height + 1)

    return score_sum


def part2(data: str) -> int:
    tmap = parse(data)
    MAP_WIDTH = len(tmap[0])
    MAP_HEIGHT = len(tmap)

    return sum(
        trailhead_scores(tmap, x, y)
        for x in range(MAP_WIDTH)
        for y in range(MAP_HEIGHT)
    )


if __name__ == "__main__":
    from run import run
    from testing import test

    test_data = open("data/test10.txt").read()
    data = open("data/day10.txt").read()

    test(part1, data=test_data, expected=36)
    test(part2, data=test_data, expected=81)

    run(part1, data)
    run(part2, data)
