import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes a list, displays the shape of the list and returns a truncated
        version of the array based on the provided start and end argument"""
    try:
        if not isinstance(family, list):
            raise TypeError("Invalid type")
        row_len = len(family[0])
        if not all(len(row) == row_len for row in family):
            raise ValueError("Inaccurate shape")
        a = np.array(family, dtype=float)
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Invalid index")
        print("My shape is :", a.shape)
        sliceStore = a[start: end]
        print("My new shape is :", sliceStore.shape)
    except Exception as e:
        print("Error:", e)
        return []
    return (sliceStore.tolist())
