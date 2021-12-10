from pathlib import Path
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import util


@util.timeit()
def part1(heights: list[list[int]]):
    """
    Naïve looping approach unfortunately, I am tired
    """
    risks = 0
    # for every point
    for y, line in enumerate(heights):
        for x, num in enumerate(line):
            # loop through 4 neighbors
            for xn, yn in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
                # check valid direction
                if yn < 0 or xn < 0 or yn >= len(heights) or xn >= len(line):
                    continue

                # lower or equal point found
                if heights[yn][xn] <= num:
                    break
            else:
                # if no lower neighbor found, increase score
                risks += num + 1
    return risks


@util.timeit()
def part2(heights: list[list[int]]):
    """
    Tried out numpy, its really weird
    scipy's ndimage.label() finds the groups nicely.
    my numpy knowledge is inefficient and strange
    """
    # prepare array "image" to a format recognized by ndimage.label
    # nonzero values bordered by 0s
    im = np.where(np.array(heights) < 9, 1, 0)

    # ndimage.label () groups consecutive areas with a unique number, bounded by 0s
    blobs, num_blobs = ndimage.label(im)
    # then we count the number of each unique label, excluding 0s
    x = np.bincount(blobs.flatten())[1:]
    # get the 3 most frequent labels
    # and return the product
    return x[np.argsort(-x)[:3]].prod()

    # to show plot
    # plt.imshow(blobs, cmap="tab20c")
    # plt.show()
    # Save the image, upscale in GIMP or PS
    # plt.imsave("plt9.png", blobs, cmap="tab20c")



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
        lines = [[int(c) for c in line] for line in lines]

    print("Part 1:", part1(lines))

    print("Part 2:", part2(lines))

    # $> Part 1: 535
    # $> Part 2: 1122700
