# Writing scripts

**Take home message:** either use `python -m` or move your scripts out of your package!

## How to call a script

**There are 2 ways you can call a script!**

Option 1:
```bash
python pythonplusplus/train.py
```

Option 2 (module option):
```bash
python -m pythonplusplus.train
```
I'll try to convince yoou that option 2 is way better!
The script just tries to do imports (see [here](../pythonplusplus/train.py))


Ok, what does it change? **sys.path**:
 1. `sys.path` will contain `./pythonplusplus`
 2. `sys.path` will contain `.`

Depending on the option you choose, the imports will work or not, (eg: trying to import `pythonplusplus/core.py`:
 - `import core`: won't work with 2, may work with 1 (depending on the rest of the package).
 - `from . import core` won't work with 1, may work with 2 (depending on the rest of the package).  
 - `from pythonplusplus import core` will work with 2, won't work with 1 unless you call `sys.path.append` to append the root directory. (check: `python pythonplusplus/train.py --append-path=.`).

**Summary:** if you have `sys.path.append` within your package, that's because you're calling your script the wrong way.

**Note:** if you want to define the behavior if `python -m pythonplusplus`, you need to define `__main__.py`

## Safety

If you're script is within a package, make sure you run instructions within `if __name__ == "__main__":` so that it does not include during imports.

## Profiling

Run with `cProfile`:
`python -m cProfile -o test.prof -m pythonplusplus.train`
Then use `snakeviz` to display:
`snakeviz test.prof`
