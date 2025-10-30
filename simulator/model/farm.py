from typing import List, TYPE_CHECKING

from simulator.model.patch import Patch
from simulator.model.plant import Plant


class Farm:
    def __init__(self, farm_id : int, plant : Plant, patch : Patch):
        self.__id = farm_id
        self.__plant = plant
        self.__patch = patch

    def __repr__(self) -> str:
        return f"{self.__plant} in a {self.__patch}"

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