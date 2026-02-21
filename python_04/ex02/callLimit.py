from typing import Any


def callLimit(limit: int):
    """
    Decorator factory that limits how many times a function can be called.

    Args:
        limit (int): Maximum number of allowed calls.

    Returns:
        A decorator that prevents the wrapped function from being
        executed more than `limit` times.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of calls to the given function.

        Args:
            function (Callable): The function to wrap.

        Returns:
            Callable: A wrapped function that can only be called `limit` times.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that calls the original function if the call limit
            has not been reached. Otherwise, prints an error message.

            Args:
                *args: Positional arguments forwarded to the wrapped function.
                **kwds: Keyword arguments forwarded to the wrapped function.

            Returns:
                The return value of the wrapped function, or None if\
                 limit exceeded.
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, *kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
