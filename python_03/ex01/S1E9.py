from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract class that is inherited from ABC abstract class"""
    try:
        def __init__(self, first_name, is_alive=True):
            """An init method for Character class"""
            self.first_name = first_name
            self.is_alive = is_alive

        @abstractmethod
        def die(self) -> None:
            """An Abstract Die function of the Character"""
            pass

    except Exception as e:
        print("Error:", e)


class Stark(Character):
    """A class inherited from Abstract character class"""
    def __init__(self, first_name, is_alive=True):
        """An init method for Stark class"""
        super().__init__(first_name, is_alive=True)

    def die(self) -> None:
        """A function that changes the health state of the
        character from True to False"""
        self.is_alive = False
