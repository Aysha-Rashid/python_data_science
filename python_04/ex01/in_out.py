def square(x: int | float) -> int | float:
    """Return the square of the given number."""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Return the number raised to the power of itself (x ** x)."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """
    Return a closure that repeatedly applies the given function
    to an internal value.

    Each call updates the stored value and returns the new result.
    """
    count = 0

    def inner() -> float:
        """Closure function that applies the provided function to the\
         internal value `x`.

        Each time this function is called:
            - The internal value `x` is updated by applying `function(x)`.
            - A call counter `count` is incremented.
            - The updated value of `x` is returned.

        Returns:
            float: The updated value after applying `function`.
        """
        nonlocal x
        nonlocal count
        count += 1
        x = function(x)
        return x
    return inner
