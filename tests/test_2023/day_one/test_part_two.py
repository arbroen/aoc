from aoc.Y2023.day_one.part_two import trebuchet


def test_trebuchet_random():
    calibrated_doc = (
        "adsf2459adfa\n"
        "adf31jhp;ui8"
    )
    assert trebuchet(calibration=calibrated_doc) == 67


def test_example():
    calibrated_doc = (
        """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
    )
    assert trebuchet(calibration=calibrated_doc) == 142


def test_trebuchet(get_test_input):
    calibrated_doc = get_test_input("day_one.txt")
    assert trebuchet(calibration=calibrated_doc) == 52840
