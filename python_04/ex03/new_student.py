import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15 char long student id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student.

    Attributes:
        name (str): Student's first name.
        surname (str): Student's last name.
        active (bool): Indicates if the student is active (default True).
        login (str): Auto-generated login (first letter of name + surname).
        id (str): Auto-generated unique identifier.
    """
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        self.login = self.name[0] + self.surname
