# **Weather Forecast Application**

## **Overview**
This Python-based weather forecast application utilizes the **Tkinter** GUI library to provide users with the current weather and a 5-day forecast for any city. It fetches data from the **OpenWeatherMap API** and displays essential weather details, such as temperature, humidity, wind speed, and a description of the weather conditions. Additionally, it features a graphical representation of the temperature trends over the next five days.

## **Features**
- **City-based Search:** Enter a city name to retrieve current weather and a 5-day forecast.
- **Detailed Weather Information:** Displays temperature, humidity, wind speed, and weather description.
- **Graphical Forecast:** Visualizes the 5-day temperature trend with a graph generated using **Matplotlib**.
- **Responsive Interface:** Built using **Tkinter** with modern fonts and styling for a smooth user experience.
- **Error Handling:** Ensures that invalid city names or failed API requests are gracefully handled.
- **Reset Functionality:** Allows users to clear input fields and weather data with the click of a button.

## **Requirements**
- Python **3.x**
- **Tkinter** (pre-installed with Python)
- **Requests:** Install with `pip install requests`
- **Matplotlib:** Install with `pip install matplotlib`
- **python-dotenv:** Install with `pip install python-dotenv`

## **Setup and Installation**

1. Clone the repository to your local machine:
    ```bash
    git clone [repository-url]
    cd [repository-directory]
    ```

2. Install the required Python packages:
    ```bash
    pip install requests matplotlib python-dotenv
    ```

3. Create a `.env` file in the root directory and add your **OpenWeatherMap API key**:
    ```ini
    API_KEY=your_openweathermap_api_key
    ```

4. Run the application:
    ```bash
    python weather_app.py
    ```

## **How It Works**
Upon entering a city name, the application retrieves the city’s geographical coordinates (latitude and longitude) via the **OpenWeatherMap Geocoding API**. Then, it fetches both the current weather and a 5-day weather forecast using the coordinates. The app displays the weather information in the main window, including the current temperature, humidity, wind speed, and a brief weather description. Additionally, the forecast is visualized as a graph with temperature trends over the next five days. The application includes error handling for invalid inputs and failed API requests.

## **Dependencies**
- **tkinter:** For building the graphical user interface.
- **requests:** For making HTTP requests to the OpenWeatherMap API.
- **matplotlib:** For generating the temperature forecast graph.
- **datetime:** For managing date and time formatting.
- **dotenv:** For securely managing the API key from an environment file.

## **API Usage**
The application interacts with the following **OpenWeatherMap APIs**:
- **Geocoding API:** To get the latitude and longitude of the entered city.
- **Current Weather API:** To retrieve the current weather conditions.
- **5 Day / 3 Hour Forecast API:** To get the weather forecast for the next five days.

## **Screenshots**
Include screenshots of the application to provide users with a visual understanding of the UI and functionality.

## **License**
This project is licensed under the **MIT License**. See the **LICENSE** file for more details.

## **Acknowledgments**
- **OpenWeatherMap** for providing weather data.
- The **Python** and **Tkinter** community for their valuable resources and tutorials.
