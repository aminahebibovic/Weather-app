import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter.font as tkfont
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct?"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


canvas = None
forecast_label = None


def get_weather(city):
    global canvas, forecast_label  


    geocoding_url = f"{GEOCODING_URL}q={city}&appid={API_KEY}"
    print(f"Pozivam API za geokodiranje: {geocoding_url}")
    
    
    response = requests.get(geocoding_url)
    
    
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch geocoding data.")
        return
    
    data = response.json()

    
    if not data:
        messagebox.showerror("Error", "City not found. Please try again.")
        return

    
    lat = data[0]["lat"]
    lon = data[0]["lon"]
    city_name = data[0]["name"]

   
    current_weather_url = f"{CURRENT_WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=en"
    print(f"Fetching current weather: {current_weather_url}")
    
    
    response = requests.get(current_weather_url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch current weather.")
        return
    
    data = response.json()

    
    main = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  

   
    weather_info = f"Temperature: {main}°C\n"
    weather_info += f"Humidity: {humidity}%\n"
    weather_info += f"Wind Speed: {wind_speed} m/s\n"
    weather_info += f"Description: {description}"

   
    weather_label.config(text=weather_info, font=font_label)
    city_time_label.config(text=f"Current time for {city_name}: {time}", font=font_label)

    
    get_forecast(lat, lon, city_name)


def get_forecast(lat, lon, city_name):
    global canvas, forecast_label  

    
    forecast_url = f"{FORECAST_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=en"
    print(f"Fetching forecast: {forecast_url}")
    
    
    response = requests.get(forecast_url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch forecast data.")
        return
    
    data = response.json()

    
    times = []
    temps = []
    humidity_vals = []
    wind_speeds = []

    for entry in data["list"]:
        timestamp = entry["dt"]
        temp = entry["main"]["temp"]
        humidity = entry["main"]["humidity"]
        wind_speed = entry["wind"]["speed"]
        time_str = datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M')

        times.append(time_str)
        temps.append(temp)
        humidity_vals.append(humidity)
        wind_speeds.append(wind_speed)

   
    plt.figure(figsize=(10, 6))
    plt.plot(times, temps, marker='o', color='#3674B5', linestyle='-', label='Temperature')
    plt.title("Weather Forecast for Next 5 Days", fontsize=16)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

  
    canvas_frame = tk.Frame(right_frame)
    canvas_frame.pack(fill="both", expand=True)

   
    forecast_header_label.config(text=f"Weather forecast for {city_name} for the next 5 days:")

  
    canvas = tk.Canvas(canvas_frame, width=500, height=300)  
    scrollbar_y = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollbar_x = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    forecast_frame = tk.Frame(canvas)

    
    for i in range(len(times)):
        forecast_info = f"Time: {times[i]} | Temp: {temps[i]}°C | Humidity: {humidity_vals[i]}% | Wind Speed: {wind_speeds[i]} m/s"
        forecast_label = tk.Label(forecast_frame, text=forecast_info, font=font_label, justify="left")
        forecast_label.pack(pady=5)

   
    canvas.create_window((0, 0), window=forecast_frame, anchor="nw")
    forecast_frame.update_idletasks()

    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")  


def reset():
    city_entry.delete(0, tk.END)  
    weather_label.config(text="")  
    city_time_label.config(text="")  
    forecast_label.config(text="")  
    if canvas:
        canvas.delete("all")  


root = tk.Tk()
root.title("Weather Forecast")


font = tkfont.Font(family="Poppins", size=14, weight="bold")  
font_label = tkfont.Font(family="Poppins", size=12)  


root.geometry("1920x1080")
root.state('zoomed')  
root.resizable(False, False)  


left_frame = tk.Frame(root, width=1200, height=1080, bg="#f1f1f1")
left_frame.pack(side="left", fill="both", expand=True, padx=30)


city_label = tk.Label(left_frame, text="Enter city name:", font=font, bg="#f1f1f1", fg="#3674B5")
city_label.pack(pady=20)

city_entry = tk.Entry(left_frame, font=font_label, width=30)
city_entry.pack(pady=20)


search_button = tk.Button(left_frame, text="Show Weather", font=font, command=lambda: get_weather(city_entry.get()))
search_button.pack(pady=20)


reset_button = tk.Button(left_frame, text="Reset", font=font, command=reset)
reset_button.pack(pady=20)


weather_label = tk.Label(left_frame, text="", font=font_label, justify="left", bg="#f1f1f1", fg="black")
weather_label.pack(pady=20)


city_time_label = tk.Label(left_frame, text="", font=font_label, justify="left", bg="#f1f1f1", fg="black")
city_time_label.pack(pady=10)


right_frame = tk.Frame(root, width=720, height=1080, bg="#ffffff")
right_frame.pack(side="right", fill="both", expand=True)


forecast_header_label = tk.Label(right_frame, text="", font=font, justify="left", bg="#ffffff", fg="#3674B5")
forecast_header_label.pack(pady=20)


root.mainloop()
