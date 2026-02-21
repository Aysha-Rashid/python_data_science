from S1E9 import Character


class Baratheon(Character):
    """Inherited Baratheon class from Character class"""
    def __init__(self, first_name, is_alive=True):
        """An init method for Baratheon class"""
        super().__init__(first_name, is_alive=True)
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "dark"

    def die(self):
        """A method that changes the health state of the
        character from True to False"""
        self.is_alive = False

    def __str__(self):
        """Return a user-friendly representation of the vector."""
        return (f"Vector : ('{self.family_name}', \
        '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Return a developer-oriented representation of the object."""
        return (f"Vector : ('{self.family_name}', \
        '{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """Inherited Lannister class from Character class"""
    def __init__(self, first_name, is_alive=True):
        """An init method for Lannister class"""
        super().__init__(first_name, is_alive=True)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """A class method function that returns a lannister object"""
        return cls(first_name, is_alive)

    def die(self):
        """A method that changes the health state of the
        character from True to False"""
        self.is_alive = False

    def __str__(self):
        """Return a user-friendly representation of the vector."""
        return (f"Vector : ('{self.family_name}', \
        '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """Return a developer-oriented representation of the object."""
        return (f"Vector : ('{self.family_name}', \
        '{self.eyes}', '{self.hairs}')")
