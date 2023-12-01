from typing import Callable

import pytest

from pathlib import Path


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    return Path(__file__).parent / "data" / "2023"


@pytest.fixture()
def get_test_input(test_data_dir) -> Callable[[str], str]:
    def _get_file(file_name: str) -> str:
        with (test_data_dir / file_name).open("r") as file:
            return file.read()

    return _get_file
