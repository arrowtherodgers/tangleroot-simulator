import abc
from typing import List

from simulator.model.farm import Farm
from simulator.model.patch import Patch
from simulator.model.plant import Plant

repo_instance = None

class IRepo(abc.ABC):
    @abc.abstractmethod
    def add_patches(self, patches : List[Patch]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_plants(self, plants : List[Plant]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def add_farms(self, farms : List[Farm]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_patches(self) -> List[Patch]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_plants(self) -> List[Plant]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_farms(self) -> List[Farm]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_plant_by_id(self, plant_id: int) -> Plant:
        raise NotImplementedError()


