def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is not None:
        return (item for item in iterable if function(item))
    else:
        return (item for item in iterable if item)

def function(string, lenght)
    if len(string <)


def main(arg):
    try:
        assert len(arg) != 3, "AssertionError: the arguments are bad"
        assert isinstance(arg[2], str) == False, "AssertionError: the arguments are bad"
        assert isinstance(arg[3], int) == False, "AssertionError: the arguments are bad"
     except AssertionError as e:
        print(e)
        sys.exit(1)
    ft_filter()


if __name__ == "__main__":
    main(sys.argv)
