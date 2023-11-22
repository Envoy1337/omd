from typing import Dict


class Pizza:
    def __init__(self, name, toppings, size: str = 'L'):
        if not isinstance(size, str):
            raise TypeError('size in string')
        self.name = name
        self.toppings = toppings
        self.size = size

    def dict(self) -> Dict[str, list]:
        return {self.name: self.toppings}

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, self.__class__) and
            self.toppings == other.toppings and
            self.size == other.size
            )
