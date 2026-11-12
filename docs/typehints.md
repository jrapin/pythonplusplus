# Type hints

## What is it? / How to add them

You have a function in `mypackage/mymodule.py`

```python
def my_function(x: float) -> float:
    return 12 / x
```

The type hints are the `float` values provided for the input parameter, and the output parameter.

## What does it do?

1. **nothing**: at runtime the type hints are absolutely ignores
2. **documentation**: this helps people that read your code understand what to provide as input / what the function returns. In the end, it will probably also help you remember it as well :)
3. **offline check**: using `mypy`, you can check that **all** your code is coherent and it only takes a few seconds without running your code!


## How do I use it


### Commandline 

Once your code is typed (or partially typed) you can run `mypy` (you may need to `uv add --dev mypy` first):
```
uv run mypy mypackage
```

It will print that everything is ok if all the types are coherent within all your package, and print issues if it finds any. Example if you have another function:

```python
def do_something_stupid(x: str) -> float:
    value = my_function(x)
    return value.replace("a", "b")
```

Then running the command will return:
```
Argument 1 to "myfunction" has incompatible type "str"; expected "float"
mypackage/test_mymodule.py:19: error: "float" has no attribute "replace"
```

Of course, just like unit tests, you can run this in a continuous integration.

**Corrolary**: for class instances, mypy will complain if you get or set an attribute that is not defined in the `__init__`, so make sure you do define **all** the attributes in the init.

Example:
```python
class Something:

    def __init__(self) -> None:
        self.an_attribute = 12

def another_function() -> None:
    something = Something()
    something.not_an_attribute = 1  # "Something" has no attribute "not_an_attribute"; maybe "an_attribute"?
```





### Linting in your IDE

There are plugins within vim, VS code and probably most others so that it prints you warnings on the fly!


## What do I need to type?

At least type function signatures:
- input parameters
- output type

**Corrolary**: it is always a bad idea to have a function that returns different types depending on the input parameters.

```python
# DONT EVER DO THIS
def do_something(return_a_tuple: bool) -> WhatTheHell:
    if return_a_tuple:
        return "a", 12
    else:
        return "b"
```

In some cases you may need to type list/dict content if you initialize it empty.

## Useful structures to know

For most classes, including your own classes, you only need to provide the type directly (see `float` above for instance). For containers however, you need to be more precise and include the type of the contained values (eg: `list[float]`)

Here are a few useful type hints (`import typing as tp`):
- `dict[str, float]`: a dict with string as keys and float as values
- `list[int]`: a list of integers
- `tuple[int]`: a tuple of exactly one integer
- `tuple[int, str]`: a tuple of 1 integer and 1 string
- `tuple[int, ...]`: a tuple of any number of integers
- `str | None`: a string or `None` (formerly `tp.Optional[str]`)
- `str | int`: a string or a int (formerly `tp.Union[str, int]`) (agaim avoid this at all cost for a function output, but it's "sort of" ok for an function input)
- `tp.Callable[[int, float], str]`: a function that takes 2 parameters, integer as the first one and float as the second, and returns a string.
- `tp.Callable[..., str]`: a function that takes an unknown number of parameters, and returns a string.
- `tp.Any`: anything, so that it basically deactivates any check on the variable. That can be useful when you don't know/don't care/when it's too much of a mess.
- `list[tp.Any]`: a list of anything

## Gotchas
- only functions with at least one type hint annotated in the signature will be checked
- non-annotated parameters will be considered `Any`
- many packages are not typed, you'll need to ignore them (see `[tool.mypy]` in [pyproject.toml](../pyproject.toml)) and all their classes will be considered as `Any`
- sometimes it takes too much time to type properly, so use type the variable as `Any`, or you can also use `# type: ignore` at the end of the line to deactivate errors. My advice: it's better to use these tricks than to give up using type hints.

```python
def another_function() -> None:
    something = Something()
    # eg: the following won't complain thanks to type: ignore
    something.not_an_attribute  # type: ignore
```


```python
def another_function() -> None:
    something: tp.Any = Something()
    # eg: the following won't complain because it's considered Any
    something.not_an_attribute 
```
