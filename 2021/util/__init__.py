from os import PathLike
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Read input")
    parser.add_argument("days", nargs="+", type=int)
    parser.add_argument("--year", type=int, default=2021)
    args = parser.parse_args()

    Aoc.yoink_input(*args.days, year=args.year)
