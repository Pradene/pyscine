def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list and prints its original and new shapes.
    Handles various errors like empty lists, incorrect types,
    and non-uniform nested lists.
    """

    if not isinstance(family, list) or \
            any(not isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")

    if not family:
        raise ValueError("family cannot be empty")

    row_length = len(family[0])

    if any(len(row) != row_length for row in family):
        raise ValueError(
            "All rows in family must have the same length"
        )

    print(f"My shape is : ({len(family)}, {row_length})")

    res = family[start:end]

    if not res:  # If slicing results in an empty list
        raise ValueError(
            "Slicing resulted in an empty list, check start and end indices"
        )

    print(f"My new shape is : ({len(res)}, {len(res[0])})")
    return res
