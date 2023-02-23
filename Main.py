import os
from typing import List
from CityListStats import CityListStats
#from GlobalWeatherManager import GlobalWeatherManager
#from WeatherReading.py import WeatherReading
#from GlobalWeatherManagerInterface.py import GlobalWeatherManagerInterface
from datetime import datetime

def main() -> None:
    file = os.path.join(os.getcwd(), "city_temperature.csv")
    eatherManager: GlobalWeatherManagerInterface = GlobalWeatherManager(file)
    readingsWithMonthAndDay: List[WeatherReading] = weatherManager.getReadings(0, 2, 1, 1)
    print("Readings with month 1 and day 1 in index 0: ", readingsWithMonthAndDay)
    readingCount: int = weatherManager.getReadingCount()
    print("Reading count: ", readingCount)
    reading0: WeatherReading = weatherManager.getReading(0)
    print("Reading at index 0: ", reading0)
    readings: List[WeatherReading] = weatherManager.getReadings(0, 10)
    print("Readings from 0 to 10: ", readings)
    cityListStats: CityListStats = weatherManager.getCityListStats("Albania", "", "Tirana")
    print("City list stats: ", cityListStats)
    iterator = weatherManager.iterator()
    count: int = 7
    print("Iterating through readings:")
    while count > 0:
        try:
            print(next(iterator))
            count -= 1
        except StopIteration:
            break
    readingsForRegression: List[WeatherReading] = weatherManager.getReadings(0, 10, 4, 23)
    temperatureLinearRegressionSlope: float = weatherManager.getTemperatureLinearRegressionSlope(readingsForRegression)
    print("Temperature linear regression slope: ", temperatureLinearRegressionSlope)
    x: List[int] = [2000, 2001, 2002]
    y: List[float] = [33.8, 42.6, 36.2]
    linearRegressionSlope: float = weatherManager.calcLinearRegressionSlope(x, y)
    print("Linear regression slope: ", linearRegressionSlope)

if __name__ == "__main__":
    main()

