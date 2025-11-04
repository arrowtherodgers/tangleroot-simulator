from typing import List

from simulator.adapters.irepo import IRepo
from simulator.model.farm import Farm
from simulator.model.patch import Patch
from simulator.model.plant import Plant


class MemoryRepo(IRepo):
    def __init__(self):
        self.__patches = list()
        self.__plants = list()
        self.__farms = list()

    def add_patches(self, patches: List[Patch]) -> None:
        self.__patches.extend(patches)

    def add_plants(self, plants: List[Plant]) -> None:
        self.__plants.extend(plants)

    def add_farms(self, farms: List[Farm]) -> None:
        self.__farms.extend(farms)

    def get_patches(self) -> List[Patch]:
        return self.__patches

    def get_plants(self) -> List[Plant]:
        return self.__plants

    def get_farms(self) -> List[Farm]:
        return self.__farms

    def get_plant_by_id(self, plant_id: int) -> List[Plant] | None:
        return next((plant for plant in self.__plants if plant.id == plant_id), None)