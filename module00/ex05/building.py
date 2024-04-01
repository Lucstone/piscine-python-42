import sys


def main(arg):
    """
    This time you have to make a real autonomous program, with a main, \
which takes a single string argument and displays the sums of its \
upper-case characters, lower-case characters, punctuation \
characters, digits, and spaces.
    • If None or nothing is provided, \
the user is prompted to provide a string.
    • If more than one argument is provided to the program, \
print an AssertionError
    """
    try:
        assert len(arg) <= 2, "AssertionError: more \
than one argument is provided"
        if len(arg) == 1 or arg[1] == "None":
            string_in_argument = ""
            while not string_in_argument:
                try:
                    string_in_argument = input("What is the text to count?\n")
                    if not string_in_argument:
                        print("Please enter a non-empty string.")
                except EOFError:
                    print("\nCTRL+D intercepted")
                    sys.exit(1)
        elif len(arg) == 2:
            string_in_argument = arg[1]
        print(f"The text contains {len(string_in_argument)} characters:")
        upper_count = sum(1 for upc in string_in_argument if upc.isupper())
        lower_count = sum(1 for lwc in string_in_argument if lwc.islower())
        punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        punct_count = sum(1 for ptc in string_in_argument if ptc in punct)
        spaces_count = sum(1 for spc in string_in_argument if spc.isspace())
        digit_count = sum(1 for dgc in string_in_argument if dgc.isdigit())
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punct_count} punctuation marks")
        print(f"{spaces_count} spaces")
        print(f"{digit_count} digits")

    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
