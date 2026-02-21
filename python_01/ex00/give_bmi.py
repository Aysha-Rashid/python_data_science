import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Takes height and weight and returns BMI"""
    try:
        if len(height) is not len(weight):
            raise ValueError("height and weight must have the same length")
        for h, w in zip(height, weight):
            if (not isinstance(h, (int, float)) or
               not isinstance(w, (int, float))):
                raise TypeError("height and weight \
                must contain only int or float")
        height = np.array(height, dtype=float)
        weight = np.array(weight, dtype=float)
        return (weight / (height ** 2)).tolist()
    except Exception as e:
        print("Error: ", e)
        return []


def apply_limit(bmi: list, limit: int) -> list[bool]:
    try:
        if not isinstance(limit, int):
            raise TypeError("Should only contain int")
        bmi = np.array(bmi, dtype=float)
        assert bmi.size > 0, "Invalid BMI"
        return (bmi > limit).tolist()
    except Exception as e:
        print("Error:", e)
        return []
