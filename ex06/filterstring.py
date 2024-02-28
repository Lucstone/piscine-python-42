import sys
from ft_filter import ft_filter


def check_char(arg):
    """
Check if all characters in the string are alphanumeric or spaces.
Return True if yes, False otherwise.
    """
    if len(arg) == 0:
        return False
    for char in arg:
        if char.isalnum() is False and char.isspace() is False:
            return False
    return True


def main(arg):
    """
Create a program that accepts two arguments: a string(S), and an integer(N). \
The program should output a list of words from S that have a length \
greater than N.
• Words are separated from each other by space characters.
• Strings do not contain any special characters. (Punctuation or invisible)
• The program must contain at least one list comprehension expression and one
lambda.
• If the number of argument is different from 2, or if the type of any \
argument is wrong,
the program prints an AssertionError.
    """
    try:
        assert len(arg) == 3, "AssertionError: the arguments are bad test"
        assert check_char(arg[1]), "AssertionError: the arguments are bad"
        assert arg[2].isdigit(), "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    words_sp = arg[1].split()
    string_filtered = ft_filter(lambda x: len(x) > int(arg[2]), words_sp)
    print(string_filtered)
    return 0


if __name__ == "__main__":
    main(sys.argv)
