import os
from typing import List, Union

PREAMBLE = 25


def part1(numbers: List[int]) -> Union[int, None]:
    for i in range(PREAMBLE, len(numbers)):
        n = numbers[i]  # Get first code after preamble

        # The previous PREAMBLE numbers
        backwards = set(numbers[i-PREAMBLE:i])

        # Check last 25 numbers for a pair that sums to n
        valid = False
        for code in backwards:
            x = n - code
            if x in backwards and x != n:
                valid = True

        # Return the first invalid number in input
        if not valid:
            return n


def part2(numbers: List[int], key: int) -> int:
    found = False
    for i in range(len(numbers)):
        sum = 0
        seen = set()
        # Iterate backwards from current number
        for num in numbers[i::-1]:
            sum += num
            seen.add(num)  # Keep track of seen numbers

            if sum > key:
                break
            elif sum == key:
                found = True
                break

        if found:
            return min(seen) + max(seen)


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as f:
        # Split input on double newlines into gro
        input = [int(line.strip()) for line in f]

    print(key := part1(input))
    print(part2(input, key))
