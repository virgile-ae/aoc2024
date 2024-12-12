from collections import Counter


def parse(data: str) -> list[tuple[int, int]]:
    return [
        (int(nums[0]), int(nums[1]))
        for line in data.splitlines()
        if (nums := line.split())
    ]


def part1(data: str) -> int:
    lists = parse(data)
    left = [row[0] for row in lists]
    right = [row[1] for row in lists]
    sorted_pairs = zip(sorted(left), sorted(right))
    return sum([abs(left - right) for (left, right) in sorted_pairs])


def part2(data: str) -> int:
    lists = parse(data)
    left = [row[0] for row in lists]
    right = [row[1] for row in lists]

    freq = Counter(right)

    return sum([num * freq[num] for num in left])


if __name__ == "__main__":
    from run import run

    data = open("data/day1.txt").read()

    run(part1, data)
    run(part2, data)
