from os import path
import re
from typing import List

# Make list of bags that can contain "shiny gold" +=
# check all bags that can contain those

# Each bag is a node in a graph, paths go from a bag to containable bags
# Start on shiny_gold node. Traverse each branch backwards, counting unique nodes encountered
# Stop when bag can not be contained (no paths terminate there)

# Nodes will be dictionary with "bag": tuple(*bags_that_contain_this_bag)

bag_holds = dict()
holds_bag = dict()


def process_input(rules: List[str]):
    line_split = re.compile(r'(\w+ \w+) bags? contain (.+)')
    contain_split = re.compile(r'(\d+)\s(\w+\s\w+)\sbags?[,.]?\s?')
    for rule in rules:
        out_bag, contains = re.match(line_split, rule).groups()
        if contains == 'no other bags.':
            inside_bags = None
        else:
            inside_bags = re.split(contain_split, contains)
            # Hacky solution to remove empty strings from re.split()
            inside_bags = tuple(filter(None, inside_bags))

            # Make set() of (count, color) tuples
            inside_bags = {c for n, c in zip(
                inside_bags[::2], inside_bags[1::2])}

            for bag in inside_bags:
                if bag in holds_bag.keys():
                    # Add to existing set
                    holds_bag[bag].add(out_bag)
                else:
                    # Create a new set with one element
                    holds_bag[bag] = {out_bag}

        bag_holds[out_bag] = inside_bags


def part1(goal: str):

    def path_search(goal):
        if goal not in holds_bag.keys():
            return set()
        return holds_bag[goal].union(*map(path_search, holds_bag[goal]))

    return len(path_search(goal))


if __name__ == "__main__":
    me = path.dirname(__file__)

    with open(path.join(me, "input.txt")) as file:
        # Split input on double newlines into groups
        rules = [line.strip() for line in file]
    process_input(rules)
    print("Part 1:", part1("shiny gold"))
    # print("Part 2:", part2(answers))
