from typing import List, Iterator

class GlobalWeatherManagerInterface:
    """
    it stores functions that manager can use or implement from
    """

    def getReadingCount(self) -> int:
        """
        Retrieves a count of readings
        """
        pass

    def getReading(self, index: int) -> WeatherReading:
        """
        Retrieves the weather reading at the specified index.
        """
        pass

    def getReadings(self, index: int, count: int) -> List[WeatherReading]:
        """
        Retrieves a set of weather readings.
        """
        pass

    def getReadings(self, index: int, count: int, month: int, day: int) -> List[WeatherReading]:
        """
        Retrieves a set of weather readings.
        """
        pass

    def getCityListStats(self, country: str, state: str, city: str) -> CityListStats:
        """
        Retrieves key list statistics for the specified country/state/city.
        """
        pass

    def iterator(self) -> Iterator[WeatherReading]:
        """
        Retrieves an iterator over all weather readings.
        """
        pass

    def getTemperatureLinearRegressionSlope(self, readings: List[WeatherReading]) -> float:
        """
        Does a linear regression analysis on the data, using x = year and y = temperature.
        """
        pass

    def calcLinearRegressionSlope(self, x: List[int], y: List[float]) -> float:
        """
        Calculates the slope of the best-fit line calculated using the Least Squares method.
        """
        pass
