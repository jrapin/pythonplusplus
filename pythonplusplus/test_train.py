import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "command",
    [
        "python -m pythonplusplus.train",
        "python pythonplusplus/train.py",
    ],
)
def test_commandline(command: str) -> None:
    cwd = Path(__file__).parents[1].absolute()
    print(f"Running from {cwd}")
    subprocess.check_call(command.split(), cwd=cwd)
