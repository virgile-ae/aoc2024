from functools import cmp_to_key


def parse_data(text: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    [rules, updates] = text.split("\n\n")

    rules = [
        (int(halves[0]), int(halves[1]))
        for line in rules.splitlines()
        if (halves := line.split("|"))
    ]
    updates = [[int(item) for item in line.split(",")] for line in updates.splitlines()]
    return (rules, updates)


def find_precedences(rules: list[tuple[int, int]]) -> dict[int, list[int]]:
    precendence_table: dict[int, list[int]] = {}

    for left, right in rules:
        if left not in precendence_table:
            precendence_table[left] = [right]
        else:
            precendence_table[left].append(right)

    return precendence_table


def is_order_right(precedences: dict[int, list[int]], update: list[int]) -> bool:
    # none of the right (i.e. the values in each dict entry) should be before the left
    return all(
        all(
            subsequent_item not in update[:index]
            for subsequent_item in precedences[page_number]
        )
        for index, page_number in enumerate(update)
        if page_number in precedences
    )


def part1(data: str) -> int:
    rules, updates = parse_data(data)
    precedences = find_precedences(rules)
    return sum(
        update[len(update) // 2]
        for update in updates
        if is_order_right(precedences, update)
    )


def part2(data: str) -> int:
    rules, updates = parse_data(data)
    precedences = find_precedences(rules)
    incorrectly_ordered_updates = [
        update for update in updates if not is_order_right(precedences, update)
    ]
    comp = lambda a, b: (1 if a in precedences and b in precedences[a] else -1)  # type: ignore
    sorted_updates: list[list[int]] = [
        sorted(update, key=cmp_to_key(comp)) for update in incorrectly_ordered_updates  # type: ignore
    ]
    return sum(update[len(update) // 2] for update in sorted_updates)


if __name__ == "__main__":
    from testing import test

    test_data = open("data/test5.txt").read()
    data = open("data/day5.txt").read()

    test(part1, data=test_data, expected=143)
    test(part2, data=test_data, expected=123)

    result1 = part1(data)
    print(f"Part 1: {result1}")
    result2 = part2(data)
    print(f"Part 2: {result2}")
