from typing import List, TYPE_CHECKING

class Patch:
    id_count = 1
    def __init__(self, category : str, location : str):
        self.__id = Patch.id_count
        Patch.id_count += 1
        self.__category = category
        self.__location = location

    def __repr__(self) -> str:
        return f"{self.__category} Patch at {self.__location}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Patch):
            return False
        return self.id == other.id

    def __lt__(self, other) -> bool:
        if not isinstance(other, Patch):
            return False
        return self.id < other.id

    def __hash__(self) -> int:
        return hash(self.id)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def category(self) -> str:
        return self.__category

    @property
    def location(self) -> str:
        return self.__location



