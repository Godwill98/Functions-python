# weather_ui.py
import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return
    
    API_KEY = 'da0de56a7eaa4f048e3153641242709'  # Replace with your actual API key
    BASE_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(BASE_URL)
        data = response.json()

        if response.status_code == 200:
            # Extract weather data
            location = data['location']['name']
            country = data['location']['country']
            temperature = data['current']['temp_c']  # Temperature in Celsius
            condition = data['current']['condition']['text']  # Weather condition

            # Display the weather information
            result_label.config(text=f"City: {location}, {country}\nTemperature: {temperature}°C\nCondition: {condition}")
        else:
            messagebox.showerror("Error", "Could not retrieve weather data")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

# Creating the main window
root = tk.Tk()
root.title("Weather App")

# Create UI elements
city_label = tk.Label(root, text="Enter City/Town:", font=('Helvetica', 15))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=('Helvetica', 12), width=30)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=('Helvetica', 12), command=get_weather)
get_weather_button.pack(pady=20)

result_label = tk.Label(root, font=('Helvetica', 12), text="")
result_label.pack(pady=20)

# Run the application
root.mainloop()
