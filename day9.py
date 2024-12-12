from itertools import repeat


class File:
    id: int | None
    start: int
    size: int

    def __init__(self, id: int | None, start: int, size: int) -> None:
        self.id = id
        self.start = start
        self.size = size

    @property
    def end(self) -> int:
        return self.start + self.size

    def checksum(self) -> int:
        if self.id is None:
            return 0
        return sum(self.id * i for i in range(self.start, self.end))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, File):
            return False
        return (
            self.id == other.id
            and self.start == other.start
            and self.size == other.size
        )


def expand_diskmap(diskmap: str) -> list[int | None]:
    hard_drive: list[int | None] = []
    for i, char in enumerate(diskmap.strip()):
        length = int(char)
        if i % 2 == 0:
            id = i // 2
            hard_drive.extend(repeat(id, length))
        else:
            hard_drive.extend(repeat(None, length))
    return hard_drive


def swap_block(hard_drive: list[int | None], index1: int, index2: int) -> None:
    temp = hard_drive[index1]
    hard_drive[index1] = hard_drive[index2]
    hard_drive[index2] = temp


def part1(data: str) -> int:
    hard_drive = expand_diskmap(data)

    left = 0
    right = len(hard_drive) - 1

    while left != right:
        if hard_drive[right] is None:
            right -= 1
        elif hard_drive[left] is not None:
            left += 1
        else:
            swap_block(hard_drive, left, right)

    return sum(i * val for i, val in enumerate(hard_drive) if val is not None)


def file_locations(diskmap: str) -> tuple[list[File], list[File]]:
    files: list[File] = []
    gaps: list[File] = []
    pointer = 0

    for i, char in enumerate(diskmap.strip()):
        length = int(char)
        if i % 2 == 0:  # Is a file
            id = i // 2
            file = File(id, pointer, length)
            files.append(file)
        else:
            gap = File(None, pointer, length)
            gaps.append(gap)
        pointer += length

    return files, gaps


def find_gap(gaps: list[File], size: int) -> tuple[int, int] | None:
    for i, gap in enumerate(gaps):
        if gap.size >= size:
            return i, gap.start


def part2(data: str) -> int:
    files, gaps = file_locations(data)

    for file in reversed(files):
        # find first gap it can move into
        maybe_gap = find_gap(gaps, file.size)
        if maybe_gap is None:
            continue

        gap_index, gap_start = maybe_gap
        # only swap if index of gap is lower than start of file
        if file.start < gap_start:
            continue

        # swap into that gap
        gap = gaps[gap_index]
        file.start = gap_start
        if file.size == gap.size:
            gaps.remove(gap)
        else:
            gap.size -= file.size
            gap.start += file.size

    return sum(file.checksum() for file in files)


if __name__ == "__main__":
    from run import run
    from testing import test

    test_data = open("data/test9.txt").read()
    data = open("data/day9.txt").read()

    test(part1, data=test_data, expected=1928)
    test(part2, data=test_data, expected=2858)

    run(part1, data)
    run(part2, data)
