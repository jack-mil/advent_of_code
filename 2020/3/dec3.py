import os
from typing import List


def part1(grid: List[str]) -> int:
    """Return the number of trees in a right 3 down 1 slope"""
    return calculate_slope(grid, 3, 1)


def part2(grid: List[str]) -> int:
    """Calculate the trees along many slopes"""
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in slopes:
        trees = calculate_slope(grid, *slope)
        print(f"slope {slope} had {trees} trees")
        product *= trees
    return product


def calculate_slope(grid: List[str], x: int, y: int) -> int:
    """General solution for any x/y slope"""
    count = 0
    height = len(grid)  # number of rows
    width = len(grid[0])  # width of rows
    column = x  # starting column
    for i in range(1, height, y):
        count += grid[i][column % width] == "#"
        column += x

    return count


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        grid: List[str] = [line.strip() for line in file]

    print("Part 1:", part1(grid))

    print("Part 2:", part2(grid))
