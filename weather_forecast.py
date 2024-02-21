# Import necessary libraries
from datetime import datetime
import requests
import argparse


# Function to retrieve hourly forecast
def get_hourly_forecast(latitude, longitude, interval, periods):
    """
    Gets hourly weather forecast for a given location.

    Arguments:
        latitude (float): Latitude coordinate of the location.
        longitude (float): Longitude coordinate of the location.
        interval (int, optional): Interval (in hours) between forecasts.
        periods (int, optional): Number of forecast periods to display.

    Returns:
        Prints the hourly forecast to the console.
    """

    # Retrieving location link
    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = requests.get(url, headers={"User-Agent": "forecaster (talzaben@andrew.cmu.edu)"})

    # Extracting data and building URL for the hourly forecast
    data = response.json()
    forecast_hourly_url = data["properties"]["forecastHourly"]

    response = requests.get(forecast_hourly_url, headers={"User-Agent": "forecaster (talzaben@andrew.cmu.edu)"})
    forecast = response.json()

    # Printing location information
    print(f"\nHourly forecast for {data['properties']['relativeLocation']['properties']['city']}, "
          f"{data['properties']['relativeLocation']['properties']['state']}:")

    # Iterating through forecast periods and printing data
    for i in range(0, periods, interval):
        # Converting to datetime object
        start_time_iso = forecast['properties']['periods'][i]['startTime']
        start_time = datetime.fromisoformat(start_time_iso)

        # Formating time for readability
        formatted_start_time = start_time.strftime('%a %I %p')

        # Extracting forecast details
        short_forecast = forecast['properties']['periods'][i]['shortForecast']
        temperature = forecast['properties']['periods'][i]['temperature']
        temperature_unit = forecast['properties']['periods'][i]['temperatureUnit']

        # Printing formatted forecast information
        print(f"\n{formatted_start_time}: {short_forecast}, {temperature} {temperature_unit}.")


def main():

    # Create argument parser with descriptions
    parser = argparse.ArgumentParser(description="Get hourly forecast for any location.")
    parser.add_argument("latitude", type=float, help="Latitude")
    parser.add_argument("longitude", type=float, help="Longitude")
    parser.add_argument("--interval", type=int, default=1, help="Interval in hours between forecasts")
    parser.add_argument("--periods", type=int, default=24, help="Number of forecast periods to display")
    args = parser.parse_args()

    # Call get_hourly_forecast function with parsed arguments
    get_hourly_forecast(args.latitude, args.longitude, args.interval, args.periods)


# Execute main function if script is run directly
if __name__ == "__main__":
    main()