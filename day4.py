VALID_XMAS_SPELLINGS = ["XMAS", "SAMX"]


def straight(data: str, position: int) -> int:
    ROW_WIDTH = data.index("\n") + 1

    horizontal = None
    # Character with the highest index in this row
    RIGHTMOST = position + 4

    if RIGHTMOST < len(data):
        horizontal = data[position : position + 4]

    vertical = None
    # Character with the highest index in this column
    BOTTOMMOST = position + ROW_WIDTH * 3

    if BOTTOMMOST < len(data):
        vertical = (
            data[position]
            + data[position + ROW_WIDTH * 1]
            + data[position + ROW_WIDTH * 2]
            + data[position + ROW_WIDTH * 3]
        )

    has_horizontal = horizontal in VALID_XMAS_SPELLINGS
    has_vertical = vertical in VALID_XMAS_SPELLINGS
    return int(has_horizontal) + int(has_vertical)


def diagonal(data: str, position: int) -> int:
    ROW_WIDTH = data.index("\n") + 1

    substring1 = None
    # Character with the highest index in this diagonal
    BOTTOM_RIGHTMOST = position + 3 * ROW_WIDTH + 3

    if BOTTOM_RIGHTMOST < len(data):
        substring1 = (
            data[position]
            + data[position + 1 * ROW_WIDTH + 1]
            + data[position + 2 * ROW_WIDTH + 2]
            + data[position + 3 * ROW_WIDTH + 3]
        )

    substring2 = None
    # Character with the highest index in this diagonal
    BOTTOM_LEFTMOST = position + 3 * ROW_WIDTH - 3

    if BOTTOM_LEFTMOST < len(data):
        substring2 = (
            data[position]
            + data[position + 1 * ROW_WIDTH - 1]
            + data[position + 2 * ROW_WIDTH - 2]
            + data[position + 3 * ROW_WIDTH - 3]
        )

    has_diagonal1 = substring1 in VALID_XMAS_SPELLINGS
    has_diagonal2 = substring2 in VALID_XMAS_SPELLINGS

    return int(has_diagonal1) + int(has_diagonal2)


def part1(data: str) -> int:
    return sum(
        straight(data, i) + diagonal(data, i)
        for i in range(len(data))
        if data[i] in "XS"
    )


VALID_MAS_SPELLINGS = ["SM", "MS"]


def x_mas(data: str, position: int) -> int:
    """Returns 1 iff there is a valid X-MAS else 0."""
    ROW_WIDTH = data.index("\n") + 1

    ABOVE_LEFT  = position - ROW_WIDTH - 1
    ABOVE_RIGHT = position - ROW_WIDTH + 1
    BELOW_LEFT  = position + ROW_WIDTH - 1
    BELOW_RIGHT = position + ROW_WIDTH + 1

    if ABOVE_LEFT < 0 or BELOW_RIGHT > len(data):
        return 0

    substring1 = data[ABOVE_LEFT] + data[BELOW_RIGHT]
    substring2 = data[ABOVE_RIGHT] + data[BELOW_LEFT]

    has_diagonal1 = substring1 in VALID_MAS_SPELLINGS
    has_diagonal2 = substring2 in VALID_MAS_SPELLINGS

    return int(has_diagonal1 and has_diagonal2)


def part2(data: str) -> int:
    return sum(x_mas(data, i) for i in range(len(data)) if data[i] == "A")


if __name__ == "__main__":
    from run import run
    from testing import test

    test_data = open("data/test4.txt").read()
    data = open("data/day4.txt").read()

    test(part1, data=test_data, expected=18)
    test(part2, data=test_data, expected=9)

    run(part1, data)
    run(part2, data)
