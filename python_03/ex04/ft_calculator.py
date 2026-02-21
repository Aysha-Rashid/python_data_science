class calculator:
    """A calculator class"""
    def __init__(self):
        """An init method for calculator class"""
        pass

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """Returns a dotproduct value"""
        cls.value = [a * b for a, b in zip(V1, V2)]
        cls.value = sum(cls.value)
        print(cls.value)

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Returns a list of int/float values after\
        adding two vectors together"""
        cls.value = [a + b for a, b in zip(V1, V2)]
        print([f"{x:.1f}" for x in cls.value])

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Returns a list of int/float values after\
        substracting two vectors together"""
        cls.value = [a - b for a, b in zip(V1, V2)]
        print([f"{x:.1f}" for x in cls.value])
