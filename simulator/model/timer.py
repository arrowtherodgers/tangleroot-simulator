class Timer:
    def __init__(self, location : str, growth_time_hrs : float, plant_id : int):
        self.__growth_time_remaining = 0.0
        self.__location = location
        self.__growth_time_hrs = growth_time_hrs
        self.__plant_id = plant_id

    @property
    def growth_time_remaining(self) -> float:
        return self.__growth_time_remaining

    @property
    def location(self) -> str:
        return self.__location

    @property
    def growth_time_hrs(self) -> float:
        return self.__growth_time_hrs

    @property
    def plant_id(self) -> int:
        return self.__plant_id

    def restart_timer(self) -> None:
        self.__growth_time_remaining = self.__growth_time_hrs

    def advance_timer(self, d_t : float) -> float:
        self.__growth_time_remaining -= d_t
        return self.__growth_time_remaining