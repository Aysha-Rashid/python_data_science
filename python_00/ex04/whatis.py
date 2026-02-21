import sys as sys


def whatis(number: int):
    if isinstance(number, int):
        if (number % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    pass


try:
    number = 0
    n = len(sys.argv)
    assert n <= 2, "more than one argument is provided"
    if n == 1 or sys.argv[1] == "":
        print("")
        sys.exit(0)
    else:
        try:
            if (sys.argv[1]):
                number = int(sys.argv[1])
        except ValueError:
            assert number == int, "argument is not an integer"
except AssertionError as error:
    print("AssertionError:", error)
    sys.exit(1)

whatis(number)
