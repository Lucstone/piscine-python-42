import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Description:
    Your function, give_bmi, takes 2 lists of integers \
    or floats in input and returns a list
    of BMI values.
    """
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi = []

    for h, w in zip(height_array, weight_array):
        assert isinstance(h, (int, float)) and isinstance(w, (int, float)), "\
        Error: The values of the lists must be integers or floats"

    assert np.size(height_array) > 0 and np.size(weight_array) > 0, "Error: \
    The size of the lists must be greater than 0"
    assert np.size(height_array) == np.size(weight_array), "Error: \
    The size of the two lists must be the same"

    for i in range(np.size(height_array)):
        assert height_array[i] > 0 and weight_array[i] > 0, "Error: \
        The values of the lists must be greater than 0"
        bmi.append(weight_array[i] / np.square(height_array[i]))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Accepts a list of integers or floats and an integer representing
    a limit as parameters. Returns a list of booleans \
    (True if above the limit).
    Handles error cases if the lists are not the same size, \
    are not int or float...
    """

    bmi_array = np.array(bmi)
    bmi_results = []
    assert isinstance(limit, int), "\
        Error: The values of the lists must be integers"
    for b in bmi_array:
        assert isinstance(b, (int, float)), "\
        Error: The values of the lists must be integers or floats"
    for b in bmi_array:
        bmi_results.append(b > limit)

    return bmi_results


def main():
    return


if __name__ == "__main__":
    main()
