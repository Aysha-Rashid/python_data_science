from typing import Any


def find_median(sorted_list: list) -> int:
    """Return the median of a sorted list of numbers."""
    if not sorted_list:
        raise ValueError("Cannot compute median of empty list")
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid] + sorted_list[mid - 1]) / 2
    return (sorted_list[mid])


def find_quartile(sorted_list: list) -> list:
    """Return the first and third quartiles (Q1 and Q3)
    using index-based calculation."""
    if len(sorted_list) < 2:
        raise ValueError("quartile: undefined (not enough data)")
    q1_index = len(sorted_list) // 4
    q3_index = (3 * len(sorted_list)) // 4
    quartile_list = [float(sorted_list[q1_index]),
                     float(sorted_list[q3_index])]
    return (quartile_list)


def find_mean(sorted_list: list) -> int:
    """Return the arithmetic mean of the numbers in the list."""
    mean_value = sum(sorted_list) / len(sorted_list)
    return (mean_value)


def find_variance(sorted_list: list) -> int:
    """Return the population variance of the numbers in the list."""
    mean_value = find_mean(sorted_list)
    var = sum(tuple(x ** 2 for x in sorted_list)) / len(sorted_list)
    var_mean = var - (mean_value ** 2)
    return (var_mean)


def find_stardDevision(sorted_list: list) -> int:
    """Return the population standard deviation of the numbers in the list."""
    var = find_variance(sorted_list)
    std_variance = var ** 0.5
    return (std_variance)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Compute and print statistical measures for the given numbers.

    Positional arguments:
        Numbers to analyze.

    Keyword arguments:
        Keys mapped to one of:
        'mean', 'median', 'quartile', 'var', or 'std'.

    Prints:
        The requested statistical results.
    """
    try:
        sorted_list = sorted(args)
        operations = {
            "mean": find_mean,
            "median": find_median,
            "quartile": find_quartile,
            "var": find_variance,
            "std": find_stardDevision
        }
        for key in kwargs:
            operation_name = kwargs[key]

            if operation_name in operations:
                if args:
                    result = operations[operation_name](sorted_list)
                    print(f"{operation_name} :", result)
                else:
                    print("ERROR")
    except Exception as e:
        print(e)
