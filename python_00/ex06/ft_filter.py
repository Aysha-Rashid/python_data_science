
def ft_filter(function, iteratable) -> list:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return (i for i in iteratable if function(i))
