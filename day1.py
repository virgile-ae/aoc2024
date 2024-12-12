from collections import Counter


def part1(data: list[tuple[int, int]]) -> int:
    left = [row[0] for row in data]
    right = [row[1] for row in data]
    sorted_pairs = zip(sorted(left), sorted(right))
    return sum([abs(left - right) for (left, right) in sorted_pairs])


def part2(data: list[tuple[int, int]]) -> int:
    left = [row[0] for row in data]
    right = [row[1] for row in data]

    freq = Counter(right)

    return sum([num * freq[num] for num in left])


if __name__ == "__main__":
    data = open("data/day1.txt").read()
    numbers = [
        (int(nums[0]), int(nums[1]))
        for line in data.splitlines()
        if (nums := line.split())
    ]

    result1 = part1(numbers)
    result2 = part2(numbers)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")
