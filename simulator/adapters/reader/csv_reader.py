import csv
from pathlib import Path
from typing import List, Set

from simulator.model.farm import Farm
from simulator.model.patch import Patch
from simulator.model.plant import Plant


class CSVReader:
    def __init__(self, data_path : Path) -> None:
        self.__data_path = data_path
        self.__plants = list()
        self.__patches = list()
        self.__farms = list()

    @property
    def plants(self) -> List[Plant]:
        return self.__plants

    @property
    def patches(self) -> List[Patch]:
        return self.__patches

    @property
    def farms(self) -> List[Farm]:
        return self.__farms

    def add_plant(self, plant : Plant) -> None:
        if not isinstance(plant, Plant):
            raise TypeError("Plant must be of type Plant")
        self.__plants.append(plant)

    def add_patch(self, patch : Patch) -> None:
        if not isinstance(patch, Patch):
            raise TypeError("Patch must be of type Patch")
        self.__patches.append(patch)

    def add_farm(self, farm : Farm) -> None:
        if not isinstance(farm, Farm):
            raise TypeError("Farm must be of type Farm")
        self.__farms.append(farm)

    def read(self) -> None:
        if not self.__data_path.exists():
            raise FileNotFoundError(f"File {self.__data_path} does not exist")

        with open(self.__data_path, mode='r', encoding='utf-8') as csv_file:
            data = csv.DictReader(csv_file)

            for row in data:
                category = row["Category"]
                seed = row["Seed"]
                payment_qty = int(row["Payment (qty)"])
                payment_type = row["Payment (type)"]
                location = row["Patch Location"]
                growth_time_hrs = float(row["Growth Time (hrs)"])
                pet_rate = int(row["Pet Rate (99)"])

                patch = next((patch for patch in self.patches if category == patch.category and location == patch.location), None)

                if patch is None:
                    patch = Patch(category, location)
                    self.add_patch(patch)

                plant = Plant(category, seed, payment_qty, payment_type, growth_time_hrs, pet_rate)
                self.add_plant(plant)

                farm = next((farm for farm in self.farms if patch == farm.patch), None)

                if farm is None:
                    farm = Farm(plant, patch)
                    self.add_farm(farm)




