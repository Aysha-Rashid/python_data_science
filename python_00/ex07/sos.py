import sys as sys


def MorseCode(string: str):
    """This is a function that takes a string and convert\
each character in it into Morse Code"""
    NESTED_MORSE = {
        " ": "/",
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

        # Digits
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }
    string = string.upper()
    for char in string:
        if char not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        return " ".join(NESTED_MORSE[char] for char in string)


def main():
    try:
        assert len(sys.argv) == 2, "Invalid number of arguments"
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1]), \
            "the arguments are bad"
        stringMorse = sys.argv[1]
        print(MorseCode(stringMorse))
    except AssertionError as error:
        print("AssertionError:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
else:
    print("not imported")
