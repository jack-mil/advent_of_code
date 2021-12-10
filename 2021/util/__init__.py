"""
Small utility package for AoC challenges

util.timeit(): function decorator to print execution time
util.Aoc.yoink_input(): download challenge input for a particular day(s)
"""
import time
import requests
import json


class Aoc:
    def __init__(self, year: str):
        self._pt1 = None
        self._pt2 = None
        self._year = year

    def reg_pt1(self, func):
        self._pt1 = func

    def reg_pt2(self, func):
        self._pt2 = func

    def run1(self):
        if self._pt1 is not None:
            self._pt1()

    def run2(self):
        if self._pt2 is not None:
            self._pt2()

    @staticmethod
    def yoink_input(*days: int, year=2021, auth_file="session.json", file: str = None):
        """
        Download input for specified days from advent of code api.

        Writes the input file to the inputs/ folder in year root directory
        """
        # Read session cookie from json file
        # {"session":"xxxxxxxxxxx"}
        with open(auth_file) as f:
            session = json.load(f)

        for day in days:
            r = requests.get(
                f"https://adventofcode.com/{year}/day/{day}/input", cookies=session
            )

            if r.status_code == 200:
                print("Grabbed input for day:", day)
                with open(f"inputs/input_{day}.txt", "w") as file:
                    file.write(r.text)
            else:
                print(r.status_code, r.text)


def timeit(print_args=False):
    """Execute a function and print it's running time"""
    def decorator(func):
        def timed(*args,**kwargs):
            ts = time.time()
            result = func(*args, **kwargs)
            te = time.time()

            if print_args:
                print(f"{func.__name__!s}: args:[ {args!s},{kwargs!s} ] took {te-ts:e} sec")
            else:
                print(f"{func.__name__!s}: took {te-ts} sec")
            return result
        return timed
    return decorator

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Read input")
    parser.add_argument("days", nargs="+", type=int)
    parser.add_argument("--year", type=int, default=2021)
    args = parser.parse_args()

    Aoc.yoink_input(*args.days, year=args.year)
