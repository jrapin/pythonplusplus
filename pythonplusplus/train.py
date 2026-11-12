import argparse
import sys
import traceback
from pathlib import Path


class Color:
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def _import(string: str) -> bool:
    print(f"\n{Color.FAIL}Attempting import: {string}{Color.ENDC}")
    try:
        exec(string)
    except Exception:
        traceback.print_exc()
        return False
    print("All good!")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Experiment with imports")
    parser.add_argument(
        "--append-path",
        type=str,
        default=None,
    )
    args = parser.parse_args()
    if args.append_path is not None:
        path = Path().absolute() / args.append_path
        print("Adding to path:", path)
        sys.path.append(str(path))
    print(f"{Color.WARNING}Current working directory:{Color.ENDC} {Path.cwd()}")
    print(
        f"{Color.WARNING}sys.path:{Color.ENDC}",
        [x for x in sys.path if "pythonplusplus" in x],
    )
    for imp in ["import core", "from . import core", "from pythonplusplus import core"]:
        _import(imp)
