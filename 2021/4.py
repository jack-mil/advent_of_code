from pathlib import Path
from copy import deepcopy

Board = list[list[int]]


def check_complete(grid: list[list[bool]]) -> bool:
    # Check rows and columns for all True
    horz = [all(line) for line in grid]

    # Transpose of 2d list using zip(*grid)
    vert = [all(col) for col in zip(*grid)]
    return any(horz) or any(vert)


def part1(inputs: list[int], boards: list[Board]) -> int:
    boards = deepcopy(boards)
    # Extra marker table to keep track of called numbers.
    # One for each board
    markers = [[[False] * 5 for _ in range(5)] for __ in range(len(boards))]

    # loop through each bingo number
    # and mark all boards where number appears
    # Also keep track of the position of called numbers using True/False
    # in markers list. This will be checked for win conditions
    for sel in inputs:
        for j, board in enumerate(boards):
            for i, line in enumerate(board):
                while sel in line:
                    # set correct position of marker board True,
                    # and set the board space to None for summation later
                    index = line.index(sel)
                    markers[j][i][index] = True
                    line[index] = None
            # win condition checking is the only difference b/w
            # part 1 and part 2. part 1 checks first board complete
            if check_complete(markers[j]):
                # Filter out the None elements, and sum each row, then sum
                # the list of rows * last pulled number
                return sel * sum(sum(filter(None, line)) for line in board)
                # return sel * sum(map(lambda x: sum(filter(None,x)), board))


def part2(inputs: list[int], boards: list[Board]) -> int:
    # Part 2 is almost identical to part 1 except for the end condition

    boards = deepcopy(boards)

    markers = [[[False] * 5 for _ in range(5)] for __ in range(len(boards))]

    for sel in inputs:
        for j, board in enumerate(boards):
            for i, line in enumerate(board):
                while sel in line:
                    markers[j][i][line.index(sel)] = True
                    line[line.index(sel)] = None
            # part 2 checks last board complete
            if all(map(check_complete, markers)):
                return sel * sum(sum(filter(None, line)) for line in board)


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
        # first line is comma seperated list of numbers
        inputs: list[int] = list(map(int, f.readline().split(",")))

        f.readline()  # seek on line down

        # split on double newlines for each board,
        # board split into lines and elements converted to ints
        boards: list[Board] = [
            [list(map(int, l.split())) for l in b.splitlines()]
            for b in f.read().split("\n\n")
        ]

    print("Part 1:", part1(inputs, boards))

    print("Part 2:", part2(inputs, boards))

    # $> Part 1: 38913
    # $> Part 2: 16836
