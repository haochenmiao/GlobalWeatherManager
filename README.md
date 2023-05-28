# GlobalWeatherManager
## About
The Global Weather Manager project is a robust and comprehensive tool. It aims to collect, process, and analyze weather data from across the globe, making it a valuable resource for climate researchers, meteorologists, and anyone interested in studying weather patterns.

## Technology Stack
The project primarily uses Python, SQL, and Tableau for data collection, management, and visualization.

## Key Components
The project contains several Python scripts that work together to collect and analyze the data:

* GlobalWeatherManager.py: This script is responsible for managing the overall workflow of the project. It calls the other scripts when necessary and ensures that everything runs smoothly.

* CityListStats.py: This script collects and processes weather data for a list of cities. The data is then stored in a SQL database for later analysis.

* WeatherReading.py: This script is used to collect detailed weather data for a specific city.

* GlobalWeatherManagerInterface.py: This is an interface script that allows the user to interact with the GlobalWeatherManager.

* Main.py: This is the main script that the user runs to start the program.

There is also a Tableau dashboard (Tableau Dashboard.twb) that provides visualizations of the data collected and analyzed by the scripts.

## SQL Usage
SQL is used extensively throughout the project for data management and analysis. It is primarily used to store the weather data collected by the Python scripts in a structured and easily accessible format. This allows the data to be queried and analyzed efficiently, which is crucial given the large amounts of data that the project deals with.

Additionally, SQL is also used to perform complex data analysis tasks. This includes calculating averages, finding maximums and minimums, and other statistical analyses. By performing these tasks in SQL, the project can take advantage of the powerful data processing capabilities of SQL databases, resulting in more efficient and faster analyses.

## How to Use
To use the GlobalWeatherManager project, clone the repository, install the necessary Python packages, and run the Main.py script. The script will guide you through the process of collecting and analyzing weather data.

## Contributions
Contributions to the GlobalWeatherManager project are welcome. Please fork the project, make your changes, and submit a pull request.

## Disclaimer
The data collected and analyzed by the GlobalWeatherManager project is intended for research purposes only. Please use the data responsibly and acknowledge the project in any publications that use the data.

## Contact
For any queries or suggestions, feel free to reach out through GitHub or the email provided in my GitHub profile.
