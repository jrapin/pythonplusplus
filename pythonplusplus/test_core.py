import difflib as dl
import re
from pathlib import Path

from . import core


def test_my_path() -> None:
    mp = core.MyPath(Path(__file__).parents[1])
    string = mp.to_str()
    print(string)
    assert string.endswith("Callback:")


def test_update_description() -> None:
    readme = Path(__file__).parents[1] / "docs" / "structure.md"
    assert readme.exists()
    text = readme.read_text("utf8")
    base = "\n## Summary of the structure\n{content}\n## Importance "
    pattern = re.compile(base.format(content="(.+?)"), re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    assert match is not None
    # replace
    lines = core.MyPath(Path(__file__).parents[1]).to_str().splitlines()
    lines[0] = "[pythonplusplus]"  # checkout folder name varies
    string = "\n".join(lines)
    text2 = pattern.sub(base.format(content=f"\n```\n{string}\n```\n"), text)
    if text2 != text:
        readme.write_text(text2)
        diffs = list(dl.unified_diff(text.splitlines(), text2.splitlines()))
        for diff in diffs:
            print(diff)
        raise ValueError(f"Had to rewrite structure.md: {diffs}")
