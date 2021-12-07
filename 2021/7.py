from pathlib import Path
import statistics


def part1(crabs: list[int]):

    median = int(statistics.median(crabs))

    return sum(abs(i - median) for i in crabs)


def part2(crabs: list[int]):

    def f(x):
        return sum((abs(x - i) * (abs(x - i) + 1)) / 2 for i in crabs)

    # Brute force solution
    # n, m = min(crabs), max(crabs)
    # return int(min(f(x) for x in range(n, m)))

    # analytical solution. mean is used based on the derivative of function f() above
    mean = int(sum(crabs) / len(crabs))
    return (int(f(mean)))


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

    # parse input and form a list of line segments defined by two points
    # line segments are a tuple of coordinate pairs
    with in_file.open() as f:
        crabs: list[int] = list(map(int, f.readline().split(",")))

    print("Part 1:", part1(crabs))

    print("Part 2:", part2(crabs))

    # $> Part 1: 349769
    # $> Part 2: 99540554
