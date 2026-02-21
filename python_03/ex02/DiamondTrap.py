from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class inherited from Baratheon and Lannister"""
    def __init__(self, first_name, is_alive=True):
        """An init method for King class"""
        super().__init__(first_name, is_alive)
        self.first_name = first_name

    @property
    def eyes(self):
        """Returns a property object"""
        return (self._eyes)

    @eyes.setter
    def eyes(self, eye_color):
        """Sets the attribute of the instance with validations"""
        try:
            if (not isinstance(eye_color, str)):
                raise TypeError("Invalid type")
            self._eyes = eye_color
        except Exception as e:
            print("Error:", e)

    @property
    def hairs(self):
        """Returns a property object"""
        return (self._hairs)

    @hairs.setter
    def hairs(self, hair_color):
        """Sets the attribute of the instance with validations"""
        try:
            if not isinstance(hair_color, str):
                raise TypeError("Invalid type")
            self._hairs = hair_color
        except Exception as e:
            print("Error:", e)

    def set_eyes(self, eye_color):
        """Tester method to set the attribute of the\
        instance with validations"""
        self._eyes = eye_color

    def get_eyes(self):
        """Tester method to return the attribute of the\
        instance with validations"""
        return (self._eyes)

    def set_hairs(self, hair_color):
        """Tester method to set the attribute of the\
        instance with validations"""
        self._hairs = hair_color

    def get_hairs(self):
        """Tester method to return the attribute of the\
        instance with validations"""
        return (self._hairs)
