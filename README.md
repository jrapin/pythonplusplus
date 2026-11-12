# Python++

Upgrade your Python skills!

> **Note:** this is old training material (written 2022–2024), kept as is. Some of it may be outdated or deprecated, so double-check against current Python and library docs.

## Package architecture
What are those `__init__.py` files for?
 - `pyproject.toml` (previously `setup.py`)
 - `__init__.py` (using it)
 - relative imports
 - pep8

See [docs/structure.md](docs/structure.md)

## Decorators
Any idea what `@property` does with your methods?
  - example
  - properties, getter/setter
  - opening: descriptors (advanced, we'll come back to it in a long long time)

See [docs/decorators.ipynb](docs/decorators.ipynb)

## Scripts
Why you are probably using `sys.path.append` in your code, while you probably shouldn't
  - scripts, commands (`if __name__ == "__main__"`)
  - `argparse`
  - `python -m mymodule.train` Vs `python mymodule/train.py` (why you end up with so many `sys.path.append`)

See [docs/scripts.md](docs/scripts.md)

## Special methods
 - `__len__`
 - `__call__`
 - `__getitem__` (slice)
 - `__repr__`
 - `__add__` `__radd__` etc...
 - `__init_subclass__`
 - extension duck typing, len and getitem enough for iterating 
   (duck typing: If it walks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.)
   gosse typing: a bit more structured: isubclass Iterable? TODO

See [docs/specialmethods.ipynb](docs/specialmethods.ipynb)

## Your Python environment
 - use uv (`uv sync`, `uv run`, `uv add`)
 - use which
 - keep your dependencies listed (`pyproject.toml`)
 - continuous integration will make sure you to have a standard environment
 - check the path it gets installed in (any .local?)
 - an activated shell may still pick a `python` from outside your env (`uv run` avoids it)
 - have you tried switching it off and on again?...

Also: simple git workflow


See [docs/install.md](docs/install.md)

## Iterator/generator/iterable
- comprehensions
- yield
- `__iter__`, `__next__`, `iter` and `next`
- extension: coroutine

See [docs/iterator-iterable-generator.ipynb](docs/iterator-iterable-generator.ipynb)  WIP

## Mutable, Immutable
How you could end up spending 2 days debugging (true story)... 
 - what are the differences? (hashable etc)
 - careful with default params, and with `3* [[0]]`
 - Side note `x = 12`, `x is 12`, `x = 1000`, `x is 1000`
 - opening with `__slot__` / `__setattr__`

See [docs/mutable-immutable.ipynb](docs/mutable-immutable.ipynb)

## Basic syntaxes (useless?)
 - quick mention on List/Dict/Set comprehensions (basic)
 - exception try except, raise, good practices
 - args, kwargs: foring args or kwargs in a signature, using `*` and `**`, tuple unpacking
 - pdb/ipdb

## Testing
Why writing (some) unit tests would probably save you time!
 - why it's useful
 - pytest example
 - continuous integration (GitHub Actions)
 - select your fights, do it little by little (and when you have a bug)

See [docs/unittests.md](docs/unittests.md)

## Type hints
How you could figure out your code is buggy without even running it
 - why it's useful (catch bugs early, including in non-executed code, documents the code)
 - how to use it
 - tricks (type ignore, tp.Any, `[tool.mypy]` config)
 - continuous integration again
 - avoid defining attributes outside init! (also useful for autocomplete etc)

See [docs/typehints.md](docs/typehints.md)


## Configuring your editor
Don't waste time doing stuff that could be automatic
 - pep8
 - ruff (format + lint)
 - mypy
 - example with vim

## Standard library part1
If you have to remember one thing: just stop using `os.path`!

See [docs/pathlib.ipynb](docs/pathlib.ipynb)

## Standard library part2
Meet your best friends:
 - collections (DefaultDict Vs setdefault, Counter)
 - itertool (product)
 - functools
 - operator
 - concurrent.futures
 - dataclasses
 - pathlib
 - tempfile
 - contextlib (saved for later :) )

See [docs/stdlib.ipynb](docs/stdlib.ipynb)

## Standard library part3/ Context: writing a buffer file context
What does `with` do in Python? Let's implement a context.
 - what is a context? (example: `with filepath.open()`)
 - enter- exit syntax
 - contextlib
 - dealing with exceptions
 - use tempfile (TemporaryDirectory) and pathlib

See [docs/contexts.ipynb](docs/contexts.ipynb)

## Arrays
- how list and arrays were represented in memory
- how to use numpy structured arrays, mmaps


## Pytorch stuff
- memory management, kernel execution, sync points
- DDP, FSDP, data loaders

## Some useful patterns:
Been there, done that
 - use dict as switches
 - `__init_subclass__`
 - dict: setdefault, pop, get(default)
 - joining a list of strings instead of appending (same with arrays, dataframe etc)

## Open sourcing
How do I make my package (nearly...) production ready?
 - precommit hooks
 - continuous integration (GitHub Actions)
 - `py.typed`
 - `[tool.mypy]` in `pyproject.toml`
 - pyprojects
 - pypi
 - LICENSE

## Advanced Python you should know but (hopefully) not use
Just so you know... but please, don't
 - metaclasses
 - `__new__`

## Very advanced Python for curious people
Where the f`*`ck does `self` come from?
 - where does self come from?
 - descriptor pattern
 - writing my own property

## WTF Python
Some Python behavior you may not have expected... 
 - private attributes with 2 underscores `__`
 - generator and variables (wtf python: evaluation time discrepancy, function inside loop sticks to the same output)
 - python's else clause for for-loops
 - etc

 See [docs/WTF-Python.ipynb](docs/WTF-Python.ipynb)

## Visualization?
- hiplot
- wandb?
- vistom?


