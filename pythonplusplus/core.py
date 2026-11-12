from pathlib import Path

from . import callbacks  # noqa: F401  # better: just use callbacks.LoggerCallback
from .callbacks.logger import LoggerCallback  # noqa: F401  # antipattern!


def is_ignored(path: Path) -> bool:
    ignore = path.suffix in (".swp", ".egg-info", ".pyc")
    ignore |= path.name in ("build", ".git", ".venv", "uv.lock", "include", "bin")
    ignore |= path.name.startswith("lib")
    ignore |= any(x in path.name for x in ("cache", "_checkpoints"))
    ignore |= path.is_dir() and path.name.startswith("_")
    return ignore


class MyPath:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def to_str(self) -> str:
        if self.path.is_file():
            strings = [self.path.name]
            if self.path.suffix in [".toml", ".py"]:
                strings += [
                    x
                    for x in self.path.read_text("utf8").splitlines()
                    if x and x[0] not in (" ", "#")
                ]
            return "\n    | ".join(strings)
        # so it's a folder
        strings = [f"[{self.path.name}]"]
        content = [MyPath(x) for x in self.path.iterdir() if not is_ignored(x)]
        content.sort(
            key=lambda p: (p.path.is_dir(), p.path.suffix == ".py", p.path.name)
        )
        for c in content:
            lines = c.to_str().splitlines()
            lines[0] = ("↳ " if c.path.is_dir() else "→ ") + lines[0]
            strings += lines
        return "\n    ".join(strings)
