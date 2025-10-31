from pathlib import Path

from simulator.adapters.irepo import IRepo
from simulator.adapters.reader.csv_reader import CSVReader


def populate(data_path : Path, repo : IRepo):
    reader = CSVReader(data_path)
    reader.read()

    plants = reader.plants
    patches = reader.patches
    farms = reader.farms

    repo.add_plants(plants)
    repo.add_patches(patches)
    repo.add_farms(farms)