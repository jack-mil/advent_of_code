import os
import re
from typing import Dict, List


def process_data(file) -> List[Dict]:
    passports = list()
    current_passport = dict()
    # Passports are split up on different lines
    for line in file:
        for field in line.split():
            name, value = field.split(":")
            current_passport[name] = value
        # Blank line signals a new passport entry
        if line == "\n":
            passports.append(current_passport)
            current_passport = dict()
    passports.append(current_passport)
    return passports


def valid_fields(id: Dict) -> bool:
    """Valid passports must have ALL of the following fields"""
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return required_fields.issubset(id.keys())


def height_check(height: str) -> bool:
    """Height must be in inches or cm, within a range depending on units"""
    if m := re.match(r"^(\d+)(in|cm)$", height):
        h = int(m.groups()[0])
        if m.groups()[1] == "in":
            return 59 <= h <= 76
        else:
            return 150 <= h <= 193
    return False


def hair_check(color: str) -> bool:
    """Hair must be a valid 6-digit hex color code (#fff000)"""
    return bool(re.match(r"^#([a-f0-9]{6})$", color))


def eye_check(color: str) -> bool:
    """Eye color must be one of the following"""
    colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return color in colors


def pid_check(pid: str) -> bool:
    """Passport number must be 9 digits (including leading 0s)"""
    return (len(pid) == 9) and (pid.isdecimal())


def valid_passport(id: Dict) -> bool:

    # To avoid missing key errors, the first step is to check for all fields
    if not valid_fields(id):
        return False

    checks = [
        1920 <= int(id["byr"]) <= 2002,  # Validate birth year
        2010 <= int(id["iyr"]) <= 2020,  # Validate issue year
        2020 <= int(id["eyr"]) <= 2030,  # Validate expiration year
        height_check(id["hgt"]),  # Validate height
        hair_check(id["hcl"]),  # Validate hair color (None if false)
        eye_check(id["ecl"]),  # Validate eye color
        pid_check(id["pid"]),  # Validate passport number
    ]
    return all(checks)


def part1(passports: List[Dict]) -> int:
    count = 0
    for id in passports:
        if valid_fields(id):
            count += 1
    return count


def part2(passports: List[Dict]) -> int:
    count = 0
    for id in passports:
        if valid_passport(id):
            count += 1
    return count


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        passports = process_data(file)

    print("Part 1:", part1(passports))
    print("Part 2:", part2(passports))
