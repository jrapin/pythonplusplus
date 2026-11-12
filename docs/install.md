# Python environment

- Creating an env should not be a pain, make it a routine :D
- Use [uv](https://docs.astral.sh/uv/): one fast tool for Python versions, environments and dependencies.

## Creating your env

From the project root:

```
uv sync          # creates .venv (with a matching Python) and installs the project + its dev group
uv run pytest    # runs a command inside the env, no activation needed
```

The notebooks in `docs/` need a few more packages: `uv sync --group notebooks`.

Add a dependency with `uv add <package>` (`uv add --dev <package>` for dev tools): it updates `pyproject.toml`.

## Simple practices

**Disclaimer**: I can't say they are the best practices, but they work well enough

- **always always always always** check where stuff are installed if you have a problem, you may be using the wrong install:
  - `which python` (or `uv run which python`)
  - `uv pip show <module>` to check where a module is installed, and which version.
  - **then again** the ground truth is actually loading the module within an interpreter, then `<the_module>.__file__` will point to the top level `__init__.py` file (also check the `__version__` field if it exists). If it's not what you expect, you're in trouble ;) (see pain points)
- keep your dependencies in `pyproject.toml` (`uv add` does it for you), so that it's easy to restart from scratch.
- keeping these dependencies up-to-date will be easier if you run continuous integration (cos it will scream at you if you don't). We'll see this another time.
- `uv sync` is the one installation command that works everywhere (local, CI, cluster). PyTorch installs the same way (`uv add torch`); for specific CUDA builds see [uv's PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/).

## My main pain points

- if you activate envs manually, the shell may still use a `python` from outside your env. Always check `which python`; `uv run` avoids the issue altogether.
- a reason I still don't understand for wrong module install path is that some stuff install or rely on `~/.local`. Deinstall and reinstall them! Or better yet, `mv .local local_backup` (once you reinstalled the content properly, it works...)


# Unrelated: git workflow

Here is a simple and efficient git workflow:

1. create a branch when you start implementing something
2. commit as often as you want on this branch (this way you can revert anything and you won't lose anything you did), don't waste time on commit messages if you don't need them, they will disappear later on.
3. check your branch on github (= have I left a "print" somewhere? am I committing files that should not be there?), give it a nice title, this is the only thing that will stay as message in the history.
4. use **squash & merge** instead of "merge" (see the dropdown menu next to merge) because it will squash all your commit into one nice commit.

Other notes:
- with the above workflow, you don't need to rebase anything ever. Rebasing is harder to perform than merging, but is supposed to be "nicer" because it keeps a single line of history. With the above workflow, we keep simple merges with a single line of history.
- don't hesitate to create new branches (eg: if you want to perform a complicated merge, create a backup branch so you're sure you can start over again)
- avoid working on main, you should only pull it from github to avoid having conflicts between origin and you. If you committed on it, change its name to a new branch (`git branch -m <new_name>`), then fetch a clean one (`git fetch origin main:main`)


