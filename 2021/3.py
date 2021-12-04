from pathlib import Path


def part1(puzzle: list[str]):
    # transpose the cols
    cols = zip(*puzzle)
    gamma = 0
    for i, col in enumerate(cols):
        # get number of ones and zeros
        ones = col.count("1")
        zeros = len(col) - ones

        # if 1s most common, increment gamma by a power of 2
        # dependent on current string index
        if ones > zeros:
            gamma += 1 << (len(puzzle[0]) - i - 1)

    mask = (1 << gamma.bit_length()) - 1
    return gamma * (gamma ^ mask)


def part2(puzzle: list[str]):
    def filter_oxy(iter: list[str], index: int):
        # count 1s and 0s
        a = [x[index] for x in iter]
        ones = a.count("1")
        zeros = len(a) - ones

        if ones >= zeros:
            iter = [x for x in iter if x[index] == "1"]
        else:
            iter = [x for x in iter if x[index] == "0"]

        if len(iter) == 1:
            return iter

        return filter_oxy(iter, index + 1)

    def filter_co2(iter: list[str], index: int):
        # count 1s and 0s
        a = [x[index] for x in iter]
        ones = a.count("1")
        zeros = len(a) - ones

        if zeros <= ones:
            iter = [x for x in iter if x[index] == "0"]
        else:
            iter = [x for x in iter if x[index] == "1"]

        if len(iter) == 1:
            return iter

        return filter_co2(iter, index + 1)

    oxy = filter_oxy(puzzle, 0)[0]
    co2 = filter_co2(puzzle, 0)[0]

    return int(oxy, base=2) * int(co2, base=2)


if __name__ == "__main__":
    day = Path(__file__).stem
    # define input file name (year and day) based on directory hierarchy
    in_file = Path(f"inputs/input_{day}.txt")

    # download the file once if needed
    if not in_file.exists():
        # modify python path so we can import a module two directories up
        from util import Aoc

        print("Downloading input")
        # Download my input from the servers. Authenticated with cookies
        Aoc.yoink_input(day, file=in_file.resolve())

    print("input: ", in_file, end="\n\n")

    with in_file.open() as f:
        puzzle: list[str] = f.read().splitlines()

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))

    # $> Part 1: 3320834
    # $> Part 2: 4481199
