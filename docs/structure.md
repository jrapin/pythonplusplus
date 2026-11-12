# Structure of a standard python package repo

## Root

Root folder should only contain README, LICENSE, and standard configuration files (Eg: pyproject.toml, .gitignore, .pre-commit-config.yaml etc)


## Summary of the structure

```
[pythonplusplus]
    → .gitignore
    → .pre-commit-config.yaml
    → .python-version
    → LICENSE
    → README.md
    → pyproject.toml
        | [build-system]
        | [project]
        | [dependency-groups]
        | [tool.setuptools.packages.find]
        | [tool.setuptools.package-data]
        | [tool.ruff]
        | [tool.ruff.lint]
        | [tool.ruff.lint.per-file-ignores]
        | [tool.mypy]
    ↳ [.github]
        ↳ [workflows]
            → ci.yml
    ↳ [docs]
        → WTF-Python.ipynb
        → contexts.ipynb
        → decorators.ipynb
        → install.md
        → iterator-iterable-generator.ipynb
        → mutable-immutable.ipynb
        → pathlib.ipynb
        → profiling.ipynb
        → scripts.md
        → specialmethods.ipynb
        → stdlib.ipynb
        → structure.md
        → typehints.md
        → unittests.md
    ↳ [pythonplusplus]
        → py.typed
        → __init__.py
            | from .core import MyPath
        → core.py
            | from pathlib import Path
            | from . import callbacks  # noqa: F401  # better: just use callbacks.LoggerCallback
            | from .callbacks.logger import LoggerCallback  # noqa: F401  # antipattern!
            | def is_ignored(path: Path) -> bool:
            | class MyPath:
        → test_core.py
            | import difflib as dl
            | import re
            | from pathlib import Path
            | from . import core
            | def test_my_path() -> None:
            | def test_update_description() -> None:
        → test_train.py
            | import subprocess
            | from pathlib import Path
            | import pytest
            | @pytest.mark.parametrize(
            | )
            | def test_commandline(command: str) -> None:
        → train.py
            | import argparse
            | import sys
            | import traceback
            | from pathlib import Path
            | class Color:
            | def _import(string: str) -> bool:
            | if __name__ == "__main__":
        ↳ [callbacks]
            → __init__.py
                | from .checkpoint import CheckpointCallback
                | from .earlystopping import EarlyStoppingCallback
                | from .logger import LoggerCallback
            → checkpoint.py
                | class CheckpointCallback:
            → earlystopping.py
                | class EarlyStoppingCallback:
            → logger.py
                | class LoggerCallback:
```

## Importance of `__init__.py`

Avoid defining classes/functions in the init file, it's only there to:
1. state the the folder is a package
2. define the interface / what is accessible
```python
import pystructure
pystructure.MyPath  # only feasible because imported in pystructure/__init__.py
```


### Anti-pattern

Often one goes very far in the package hieararchy to find something they need eg: `from .callbacks.logger import LoggerCallback`. A better pattern is to gather the few import classes / functions of your (sub-)package within the `__init__`. In this example, we gather important classes in `callbacks/__init__.py` so that we can access any callback by just having `from . import callbacks`. This has a number of advantages, including:

- **simpler / more readable**: just remember that all callbacks are in `callbacks`, you don't have to dive deep into package hieararchy.
- **more flexible / less coupling**: the `__init__.py` ends up being your external API for the package, how it's structured inside does not matter so you can update it / restructure it without any consequence for the rest of your code.

**Note**: the only case I would not recommend this is if loading one of the module takes a lot of time.


# Conventions

## Naming
If you are not familiar with [pep8](https://www.python.org/dev/peps/pep-0008/), go read it! It's a set of convention for Python programming, 
because consistency helps readability.

In particular, in term of namings:
- **classes**: normally use capitalized words, eg `MyClass`
- **functions/methods/variables/attributes**: use underscores, eg `my_method()`, `my_variable`
- **packages/modules**: use lowercase without underscore (if readable): `mymodule`

When defining non-public attributes/methods (not meant to be used from outside your class), use a leading underscore `_my_private_attribute`. 

FYI: Using 2 underscores leads to more complex behavior... it's safer to avoid it.
