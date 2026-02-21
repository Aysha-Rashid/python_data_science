def Print(output):
    print(output)


class calculator:
    """A calculator class"""
    def __init__(self, vector):
        """An init method for calculator class"""
        self.vector = [float(x) for x in vector]

    def __add__(self, object) -> None:
        """Returns a List of int/floats values after adding them"""
        self.vector = [x + object for x in self.vector]
        print([f"{x:.1f}" for x in self.vector])
        pass

    def __mul__(self, object) -> None:
        """Returns a List of int/floats values after multiplying them"""
        self.vector = [x * object for x in self.vector]
        print([f"{x:.1f}" for x in self.vector])
        pass

    def __sub__(self, object) -> None:
        """Returns a List of int/floats values after substracting them"""
        self.vector = [x - object for x in self.vector]
        print([f"{x:.1f}" for x in self.vector])
        pass

    def __truediv__(self, object) -> None:
        """Returns a List of int/floats values after diving them"""
        if (object != 0):
            self.vector = [x / object for x in self.vector]
            print([f"{x:.1f}" for x in self.vector])
        else:
            raise ZeroDivisionError("division by zero is wrong")
        pass
