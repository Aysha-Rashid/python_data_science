import sys as sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "The arguments are bad"
        stringS = sys.argv[1]
        number = 0
        try:
            number = int(sys.argv[2])
            assert all(c.isalnum() or c == ' ' for c in stringS), \
                "Contains invalid characters"
        except ValueError:
            assert number == int, "Integer Invalid type"
    except AssertionError as error:
        print("AssertionError:", error)
        sys.exit(1)
    splitList = stringS.split()
    TheFiltered = ft_filter(lambda word: len(word) > number, splitList)
    print(list(TheFiltered))
    sys.exit(0)


if __name__ == '__main__':
    main()
