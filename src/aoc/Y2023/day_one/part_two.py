import re


digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern = "(?=(" + "|".join(digit_map.keys()) + "|\\d))"


def get_numbers(line: str) -> list[str]:
    matches = re.findall(pattern, line)

    return [digit_map[match] if match in digit_map else match for match in matches]


def trebuchet(calibration: str) -> int:
    count = 0

    for line in calibration.split():
        numbers = get_numbers(line=line)
        count += int(f"{numbers[0]}{numbers[-1]}")

    return count
