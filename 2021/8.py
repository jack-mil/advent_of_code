from pathlib import Path
from itertools import permutations
from util import timeit


def part1(lines):
    """Count digits 1 4 7 or 8 in output
    1: 2 segments
    7: 3 segments
    4: 4 segments
    8: 7 segments"""
    outputs = [n[1] for n in lines]
    chk = lambda x: x in (2, 3, 4, 7)
    return len(list(filter(chk, map(len, sum(outputs, [])))))


@timeit()
def part2(lines):
    """Decode the jumbled lines of led segments"""
    decoder = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    abc = "abcdefg"

    count = 0
    # brute force check all 5040 combinations. not that many really
    for perm in permutations(abc):
        mapping = dict(zip(perm, abc))
        for line, output in lines:
            lookup = dict()
            for seq in line:
                seq = "".join(sorted(seq))
                conv = "".join(sorted(str.translate(seq, str.maketrans(mapping))))
                # if this permutation doesn't work for this line, immediately move onto next one
                try:
                    lookup[seq] = decoder[conv]
                except KeyError:
                    break

            # code for this line cracked
            # only occurs for one specific permutation
            if len(set(lookup.values())) == 10:
                count += sum(
                    lookup["".join(sorted(x))] * (10 ** (len(output) - n - 1))
                    for n, x in enumerate(output)
                )

    return count


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
        lines = f.read().splitlines()
        lines = [[n.split() for n in line.split(" | ")] for line in lines]

    print("Part 1:", part1(lines))

    print("Part 2:", part2(lines))

    # $> Part 1: 421
    # $> Part 2: 986163
