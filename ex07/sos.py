import sys


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


def ft_sos(arg):
    """
Make a program that takes a string as an argument and encodes \
it into Morse Code.
• The program supports space and alphanumeric characters
• An alphanumeric character is represented by dots . and dashes -
• Complete morse characters are separated by a single space
• A space character is represented by a slash /
    """

    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }
    morse_string = ""
    for char in arg:
        morse_string += NESTED_MORSE[char.upper()] + " "
    return morse_string.rstrip()


def main(arg):
    try:
        assert len(arg) == 2, "AssertionError: the arguments are bad"
        assert check_char(arg[1]), "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    print(f"{ft_sos(arg[1])}")
    return


if __name__ == "__main__":
    main(sys.argv)
