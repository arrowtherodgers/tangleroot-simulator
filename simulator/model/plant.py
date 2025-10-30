from typing import List, TYPE_CHECKING

class Plant:
    def __init__(self, plant_id : int, category : str, seed : str, payment_qty : int, payment_type : str, growth_time_hrs : float, pet_rate : int):
        self.__id = plant_id
        self.__category = category
        self.__seed = seed
        self.__payment_qty = payment_qty
        self.__payment_type = payment_type
        self.__growth_time_hrs = growth_time_hrs
        self.__pet_rate = pet_rate

    def __repr__(self) -> str:
        return f"{self.__seed} Plant"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Plant):
            return False
        return self.id == other.id

    def __lt__(self, other) -> bool:
        if not isinstance(other, Plant):
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
    def seed(self) -> str:
        return self.__seed

    @property
    def payment_qty(self) -> int:
        return self.__payment_qty

    @property
    def payment_type(self) -> str:
        return self.__payment_type

    @property
    def growth_time_hrs(self) -> float:
        return self.__growth_time_hrs

    @property
    def pet_rate(self) -> int:
        return self.__pet_rate

