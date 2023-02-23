from typing import Tuple

class WeatherReading:
    def __init__(self, region: str, country: str, state: str, city: str, month: int, day: int, year: int,
                 avgTemperature: float):
        self.region = region
        self.country = country
        self.state = state
        self.city = city
        self.month = month
        self.day = day
        self.year = year
        self.avgTemperature = avgTemperature

    def region(self) -> str:
        return self.region

    def country(self) -> str:
        return self.country

    def state(self) -> str:
        return self.state

    def city(self) -> str:
        return self.city

    def month(self) -> int:
        return self.month

    def day(self) -> int:
        return self.day

    def year(self) -> int:
        return self.year

    def avgTemperature(self) -> float:
        return self.avgTemperature

    def __eq__(self, other: 'WeatherReading') -> bool:
        if isinstance(other, WeatherReading):
            return (self.country == other.country
                    and self.state == other.state
                    and self.city == other.city
                    and self.year == other.year
                    and self.month == other.month
                    and self.day == other.day
                    and self.avgTemperature == other.avgTemperature)
        return False

    def __lt__(self, other: 'WeatherReading') -> bool:
        if isinstance(other, WeatherReading):
            if self.country != other.country:
                return self.country < other.country
            elif self.state != other.state:
                return self.state < other.state
            elif self.city != other.city:
                return self.city < other.city
            elif self.year != other.year:
                return self.year < other.year
            elif self.month != other.month:
                return self.month < other.month
            else:
                return self.day < other.day
        raise ValueError(f"Cannot compare {type(self)} to {type(other)}")

    def compareCityState(self, country: str, state: str, city: str) -> int:
        if self.country != country:
            return self.country < country
        elif self.state != state:
            return self.state < state
        else:
            return self.city < city

    def __str__(self) -> str:
        return (f"WeatherReading{{country='{self.country}', state='{self.state}', city='{self.city}', "
                f"month={self.month}, day={self.day}, year={self.year}, avgTemperature={self.avgTemperature}}}")
