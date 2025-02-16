Weather Forecast Application
Description
This is a weather forecast application built using Python and the Tkinter GUI library. It fetches current weather and a 5-day forecast for a specified city using the OpenWeatherMap API. The application displays weather details such as temperature, humidity, wind speed, and a description of the current conditions. It also provides a graphical representation of the forecast for the next five days.

Features
Search for current weather and a 5-day forecast by city name.
Displays temperature, humidity, wind speed, and weather description.
Graphical representation of the 5-day temperature trend using Matplotlib.
Responsive user interface built with Tkinter, featuring modern fonts and styling.
Error handling for invalid city names or failed API requests.
Reset button to clear input fields and weather data.
Requirements
Python 3.x
Tkinter (included with most Python installations)
Requests: pip install requests
Matplotlib: pip install matplotlib
python-dotenv: pip install python-dotenv
OpenWeatherMap API Key
Setup and Installation
Clone this repository to your local machine:
bash
Copy
git clone <repository-url>
cd <repository-folder>
Install the required Python packages:
bash
Copy
pip install requests matplotlib python-dotenv
Create a .env file in the root directory and add your OpenWeatherMap API key:
ini
Copy
API_KEY=your_openweathermap_api_key
Run the application:
bash
Copy
python weather_app.py
How It Works
The application prompts the user to enter a city name.
It fetches the geographical coordinates (latitude and longitude) of the city using the OpenWeatherMap Geocoding API.
It then retrieves current weather data and a 5-day forecast using the city’s coordinates.
The weather information is displayed in the main window, including temperature, humidity, wind speed, and a short description.
The 5-day forecast is visualized in a graph using Matplotlib.
The application is equipped with error handling for invalid inputs or failed API requests.
Dependencies
tkinter: For building the graphical user interface.
requests: For making HTTP requests to the OpenWeatherMap API.
matplotlib: For generating the forecast graph.
datetime: For handling date and time formatting.
dotenv: For securely loading the API key from an environment variable.
API Usage
This application uses the following OpenWeatherMap APIs:

Geocoding API: To get latitude and longitude of the entered city.
Current Weather API: To get the current weather conditions.
5 Day / 3 Hour Forecast API: To get the weather forecast for the next five days.
Screenshots
Include screenshots of the application in action to give users a better idea of the UI and features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
OpenWeatherMap for providing weather data.
Python and the Tkinter community for resources and tutorials.