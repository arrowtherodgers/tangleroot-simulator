from typing import List, TYPE_CHECKING

from simulator.model.patch import Patch
from simulator.model.plant import Plant

class Farm:
    id_count = 1
    def __init__(self, plant : Plant, patch : Patch):
        self.__id = Farm.id_count
        Farm.id_count += 1
        self.__plant = plant
        self.__patch = patch

    def __repr__(self) -> str:
        return f"{self.__plant} from a {self.__patch}"

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
    def plant(self) -> Plant:
        return self.__plant

    @property
    def patch(self) -> Patch:
        return self.__patch