

def get_first_number(line: str) -> str:
    for character in line:
        if character.isdigit():
            return character
    else:
        Exception("Non found, erroneous input")


def trebuchet(calibration: str) -> int:
    count = 0

    for line in calibration.split():
        count += int(
            f"{get_first_number(line=line)}{get_first_number(line=line[::-1])}"
        )

    return count
