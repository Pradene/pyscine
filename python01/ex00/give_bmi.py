def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[float]:
    """
    This function takes two lists (heights and weights),
    computes the BMI (Body Mass Index) if the lengths of both lists are equal,
    and returns the result as a list.
    """

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists")

    if any(not isinstance(h, (int, float)) for h in height) or \
            any(not isinstance(w, (int, float)) for w in weight):
        raise TypeError(
            "All elements in height and weight must be integers or floats"
        )

    if len(height) != len(weight):
        raise ValueError("height and weight lists must have the same length")

    if any(h <= 0 for h in height):
        raise ValueError(
            "height values must be greater than zero to compute BMI"
        )

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """
    This function takes a list of BMI (Body Mass Index) values
    and checks if each value is greater than a given limit.
    Returns a list of boolean values.
    """

    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if any(not isinstance(value, (int, float)) for value in bmi):
        raise TypeError("All elements in bmi must be integers or floats")

    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an integer or float")

    return [value > limit for value in bmi]
