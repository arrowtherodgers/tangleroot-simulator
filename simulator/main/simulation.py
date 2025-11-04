from typing import List, Optional
import random

from simulator.adapters.irepo import IRepo
from simulator.model.plant import Plant
from simulator.model.timer import Timer

from collections import Counter

SIGMA = 0.5
EXCLUSIONS = ["Crystal Tree"]

class SimulationOutput:
    def __init__(self, pet_obtained: bool, harvests : List[Plant], days_elapsed : int, final_patch_location : Optional[str] = None):
        self.__pet_obtained = pet_obtained
        self.__harvests = harvests
        self.__days_elapsed = days_elapsed
        self.__final_patch_location = final_patch_location or ""

    @property
    def pet_obtained(self) -> bool:
        return self.__pet_obtained

    @property
    def days_elapsed(self) -> int:
        return self.__days_elapsed

    def result(self) -> str:
        if self.__pet_obtained:
            harvest = self.__harvests[-1]
            location = self.__final_patch_location
            seed = harvest.seed
            return f"Pet obtained: from {seed} harvested from {location}. Total harvests: {len(self.__harvests)} over {self.__days_elapsed} days."
        return f"No pet obtained. Total harvests: {len(self.__harvests)} over {self.__days_elapsed} days."

    def count_harvests(self) -> Counter:
        return Counter(plant.seed for plant in self.__harvests)

class Simulation:
    def __init__(self, repo : IRepo, max_farm_runs_per_day : int, max_active_hours : int, max_days_to_run : int):
        self.__repo = repo

        self.__max_farm_runs_per_day = max_farm_runs_per_day
        self.__max_active_hours = max_active_hours
        self.__max_days_to_run = max_days_to_run

        self.__timers = list()

    def initialize(self):
        patches = self.__repo.get_patches()
        plants = self.__repo.get_plants()
        for patch in patches:
            if patch.category in EXCLUSIONS:
                continue
            location = patch.location
            plant = next(plant for plant in plants if patch.category == plant.category)
            if not plant:
                continue

            growth_time_hrs = plant.growth_time_hrs
            plant_id = plant.id
            timer = Timer(location, growth_time_hrs, plant_id)
            timer.restart_timer()
            self.__timers.append(timer)

    def get_random_interval(self) -> float:
        noise = random.gauss(0, SIGMA)
        return max(0.0, round((self.__max_active_hours / self.__max_days_to_run) + noise, 2))

    def run(self) -> SimulationOutput:
        harvests = list()

        for d in range(self.__max_days_to_run):
            time_elapsed = 0.0
            farm_runs = 1

            while time_elapsed < self.__max_active_hours and farm_runs < self.__max_farm_runs_per_day:
                interval_elapsed = self.get_random_interval()
                for timer in self.__timers:
                    time_remaining = timer.advance_timer(interval_elapsed)
                    if time_remaining < 0:
                        plant = self.__repo.get_plant_by_id(timer.plant_id)
                        harvests.append(plant)
                        if plant.roll_pet():
                            return SimulationOutput(True, harvests, d, timer.location)
                        timer.restart_timer()
                time_elapsed += interval_elapsed
                farm_runs += 1

            inactive_interval = max(0.0, 24.0 - time_elapsed)
            for timer in self.__timers:
                timer.advance_timer(inactive_interval)

        return SimulationOutput(False, harvests, self.__max_days_to_run)


