import os
from typing import List, Tuple, Union


def machine(instructions: List[str]) -> Tuple[int, bool]:
    """
    Run a set of instructions. Returns a tuple of the form (count, no_loops)
    If a loop is detected, will return the value of the accumulator just before
    the first repeated instruction. Otherwise returns (count, True)
    """
    seen_lines = set()
    count = 0
    line = 0
    while line not in seen_lines:
        if line >= len(instructions):
            return count, True
        inst, n = instructions[line].split()
        n = int(n)
        seen_lines.add(line)
        if inst == "nop":
            line += 1
        elif inst == "acc":
            line += 1
            count += n
        elif inst == "jmp":
            line += n

    return count, len(seen_lines) == len(instructions)


def part1(instructions: List[str]):
    """Run given instructions and return the count just before a loop is detected"""
    return machine(instructions)[0]


def part2(instructions: List[str]) -> Union[int, None]:
    """
    Brute force approach to part 2. Swap every nop/jmp command one-at-a-time
    and check for loops. Return the accumulator of the first modified
    instruction set that does not loop
    """
    for i, line in enumerate(instructions):
        inst, n = line.split()
        new_insts = instructions[::]
        if inst == "nop":
            new_insts[i] = "jmp " + n
        elif inst == "jmp":
            new_insts[i] = "nop " + n
        count, no_loops = machine(new_insts)
        if no_loops:
            return count
    return None


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        # Split input on double newlines into groups
        answers = [line.strip() for line in file]

    print("Part 1:", part1(answers))
    print("Part 2:", part2(answers))
