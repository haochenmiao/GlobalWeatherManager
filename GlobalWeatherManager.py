import os
import sys
import bisect
from typing import List
from datetime import date
from WeatherReading import WeatherReading
from CityListStats import CityListStats
from GlobalWeatherManagerInterface import GlobalWeatherManagerInterface


class GlobalWeatherManager(GlobalWeatherManagerInterface):
    """
    Stores and retrieves a collection of weather readings,
    provides methods to retrieve statistics about weather readings
    for a given country, state and city.
    """

    def __init__(self, temperature_file):
        """
        Reads the weather data file and sorts them into the readings list.
        """
        self.readings = []
        with open(temperature_file, "r") as f:
            next(f)  # skip header line
            for line in f:
                fields = line.strip().split(",")
                region, country, state, city = fields[:4]
                month, day, year = map(int, fields[4:7])
                avg_temperature = float(fields[7])
                wr = WeatherReading(region, country, state, city, date(year, month, day), avg_temperature)
                self.readings.append(wr)
        self.readings.sort()

    def get_reading_count(self):
        """
        Retrieves a count of readings.
        """
        return len(self.readings)

    def get_reading(self, index):
        """
        Retrieves the weather reading at the specified index.
        """
        return self.readings[index]

    def get_readings(self, index, count):
        """
        Retrieves a set of weather readings.
        """
        if index < 0 or index >= len(self.readings):
            raise ValueError("Invalid index")
        if count < 1:
            raise ValueError("Invalid count")
        if index + count > len(self.readings):
            raise ValueError("Index + count is greater than the total readings count")
        return self.readings[index:index + count]

    def get_readings_by_date(self, index, count, month, day):
        """
        Retrieves a set of weather readings matching the specified criteria.
        """
        result = []
        for wr in self.readings:
            if wr.date.month == month and wr.date.day == day:
                result.append(wr)
                if len(result) == count:
                    break
        return result

    def get_city_list_stats(self, country, state, city):
        """
        Retrieves key list statistics for the specified country/state/city.
        """
        index = self._binary_search_city(self.readings, country, state, city)
        if index == -1:
            return None
        else:
            return self._compute_stats(self.readings, index)

    @staticmethod
    def _binary_search_city(readings, country, state, city):
        """
        Searches for the index of the first weather reading that matches the specified country/state/city.
        Returns -1 if not found.
        """
        target = (country, state, city)
        i = bisect.bisect_left(readings, target)
        if i != len(readings) and readings[i].country == country and readings[i].state == state and readings[
            i].city == city:
            return i
        else:
            return -1

    @staticmethod
    def _compute_stats(readings, index):
        """
        Computes the list stats for the weather readings starting at the specified index.
        """
        stats = CityListStats()
        for city in city_list:
            stats.update(city)
        print("Average population: ", stats.get_average_population())
        print("Average area: ", stats.get_average_area())

    def getTemperatureLinearRegressionSlope(self, cityName):
        city = self.getCity(cityName)
        if city is not None:
            return city.getTemperatureLinearRegressionSlope()
        return None

    def calcLinearRegressionSlope(self, x, y):
        n = len(x)
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        numerator = sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)])
        denominator = sum([(x[i] - x_mean) ** 2 for i in range(n)])
        return numerator / denominator if denominator != 0 else None

    def getCity(self, cityName):
        for city in self.cities:
            if city.getName() == cityName:
                return city
        return None



