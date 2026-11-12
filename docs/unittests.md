# Unit tests

## What is it? / How to do one?

You have a function in `mypackage/mymodule.py`:

```python
def my_function(x: float) -> float:
    return 12 / x
```

Instead of manually testing that this function does what you expect,
write it down as a test!
Create a new module `mypackage/test_mymodule.py` (the exact name or location does not matter,
as long as the name starts with `test_`):


```python
# the function name does not really matter as long as it starts with test_
def test_my_function() -> None:
    output = my_function(12)
    # let's check if it's what we expect
    assert  output == 1
```

Then `uv add --dev pytest` if you don't have it yet, and run:
```
uv run pytest mypackage --verbose
```

You should see a line:
```
mypackage/test_mymodule.py::test_my_function PASSED
```

You could add more tests, example: you expect your function to not raise any exception
if the input is 0:

```python
def test_my_function() -> None:
    output = my_function(12)
    # let's check if it's what we expect
    assert  output == 1

def test_my_function_zero() -> None:
    my_function(0)
```

This time you should see
```
mypackage/test_mymodule.py::test_my_function PASSED
mypackage/test_mymodule.py::test_my_function_zero FAILED
```

## Why you should use unit tests

- instead of trying your function once manually, you leave a tests that you can run regularly/automatically. This way
  you're sure your function will always do what you expect.
- when you have a bug, reproduce the bug through a test, then fix it, then you're sure you'll never have the same bug again.
- when you start having multiple tests covering your code, if you modify something in one place, you can run the tests
  to figure out you did not break something somewhere you did not expect.
- on the long term, you'll think about how to test a function at the same time as you implement it. 
  That will push you towards implementing simpler/more flexible functions that do one thing and do it well, 
  instead of complex functions which can be hard to use. This mindset is very beneficial on the long term!

## What is Continuous Integration?

Continuous integration is the use of a external tool to run your test automatically.
GitHub Actions is integrated with GitHub, and can run your code automatically at each PR and show
within your PR if the tests passed or did not!

**Benefits**:
- if you are working with other people, you're sure their PRs won't break your code.
- if you working with yourself, you're sure their PRs won't break your code (...)
- because the tests run another machine you need to provide instructions on how to install your settings. This
  is useful to keep requirements up-to-date, and provides a way for new users to have working installation steps.

See [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) for this repository's own setup.
