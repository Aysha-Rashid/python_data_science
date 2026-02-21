import sys as sys


def countString(StringToCount: str):
    """This function is to count the uppercase, lowercase, isdigit, \
punctuation and space in the string"""
    upperCase = 0
    lowerCase = 0
    isDigit = 0
    punctuation = 0
    space = 0
    for i in StringToCount:
        if i.isupper():
            upperCase += 1
        elif i.islower():
            lowerCase += 1
        elif i.isdigit():
            isDigit += 1
        elif not i.isalnum() and not i.isspace():
            punctuation += 1
        elif i.isspace():
            space += 1
    totalChar = upperCase + lowerCase + punctuation + space + isDigit
    print("The text contains", totalChar, "characters:")
    print(upperCase, "upper letters")
    print(lowerCase, "lower letters")
    print(punctuation, "punctuation marks")
    print(space, "spaces")
    print(isDigit, "digits")
    pass


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            print("What is the text to count?")
            userInput = sys.stdin.read()
        else:
            userInput = sys.argv[1]
    except AssertionError as error:
        print("AssertionError:", error)
        sys.exit(1)
    countString(userInput)


if __name__ == '__main__':
    main()
