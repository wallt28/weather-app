# Flask Weather App

This is a basic web server application hosted on Flask that allows a user to retrieve the weather forecast for a particular city.

## Usage

1.  Open your terminal and navigate to the directory where the app is located
2.  Run the command `flask run`
3.  Open your preferred web browser and navigate to `http://127.0.0.1:5000/`
4.  Enter the city name in the input field and click the "Check City" button
5.  The web server will retrieve the weather forecast from OpenWeatherMap API and send an HTML page containing the forecast back to the user.

## Installation

To install and use this app:

1.  Clone this repository to your local machine
4.  Install the required dependencies by running `pip install -r requirements.txt`
5.  In the '.env` add your OpenWeatherMap API key to the file (https://openweathermap.org/api)
6.  Run the command `flask run` to start the server

## API Reference

This app uses the OpenWeatherMap API to retrieve weather forecast data. To use this app, you will need to obtain an API key from OpenWeatherMap and add it to the `.env` file.

## Contributing

Contributions are welcome. Please open an issue or pull request if you would like to contribute to this project.
