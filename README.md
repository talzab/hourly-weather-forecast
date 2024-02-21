# Hourly Weather Forecast
This Python script uses the National Weather Service API to provide an easy-to-use command-line interface for retrieving hourly weather forecasts for any location. By supplying latitude and longitude coordinates, users can customize the forecast interval and the number of periods to display.

## How to Use
1. Make sure you have Python installed on your system.
   
2. Clone this repository to your local machine:
   
`
git clone https://github.com/your-username/weather-forecaster.git
`

3. Navigate to the project directory:
   
`
cd hourly-weather-forecaster
`

4. Install the required libraries using:
   
`
pip install requests
`

5. Run the script with the following command:
   
`
python weather_forecaster.py latitude longitude [--interval INTERVAL] [--periods PERIODS]
latitude (float): Latitude coordinate of the location.
longitude (float): Longitude coordinate of the location.
--interval (int, optional): Interval (in hours) between forecasts. Default is 1.
--periods (int, optional): Number of forecast periods to display. Default is 24.
`
Example:
`
python weather_forecaster.py 40.7128 -74.0060 --interval 2 --periods 12
`

This example fetches the hourly forecast for New York City, with a 2-hour interval for the next 12 periods.
