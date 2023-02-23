from typing import List

class CityListStats:
    def init(self, startingIndex: int, count: int, years: List[int]):
        self.startingIndex = startingIndex
        self.count = count
        self.years = years

    def __str__(self):
        return f"CityListStats{{startingIndex = {self.startingIndex}, count = {self.count}, years = {self.years}}}"
