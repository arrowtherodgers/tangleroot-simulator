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

