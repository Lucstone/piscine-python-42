import sys

if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
        if len(sys.argv) == 2:
            try:
                assert isinstance(int(sys.argv[1]), int)
            except ValueError:
                print("AssertionError: argument is not an integer")
                sys.exit(1)
    except AssertionError as e:
        print(e)
        sys.exit(1)

    if len(sys.argv) == 2:
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")