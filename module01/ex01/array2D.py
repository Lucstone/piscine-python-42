import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
   Description:
        Write a function that takes as parameters a 2D array,
 prints its shape, and returns a
truncated version of the array based on the provided start and end arguments.
You must use the slicing method.
You have to handle error cases if the lists are not the same size,
are not a list ...
    """
    try:
        if not isinstance(family, list) or not isinstance(start, int):
            raise AssertionError("Input must be a list and 2 integers.")
        if not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integers.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")

        original_shape = np.array(family).shape
        print(f"My shape is: {original_shape}")

        truncated_array = np.array(family)[start:end].tolist()
        truncated_shape = np.array(truncated_array).shape
        print(f"My new shape is: {truncated_shape}")

        return truncated_array
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return None


def main():
    return


if __name__ == "__main__":
    main()
