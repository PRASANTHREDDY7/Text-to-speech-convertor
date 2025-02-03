import requests

#enter your api_key and this is my api_key
API_KEY = "2aa93f093b41ba8fa397ef94b2b8c69d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    # Request weather data from the API
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(request_url)

    # Check if the request was successful 200 means it is successful
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # it will Display the weather information
        print(f"Weather in {city_name}:")
        print(f"- Condition: {weather}")
        print(f"- Temperature: {temperature}°C")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind Speed: {wind_speed} m/s")
    else:
        print("Error fetching weather data. Please check the city name or API key.")

def main():
    print("Welcome to the Weather App!")
    city_name = input("Enter the city name: ")
    get_weather(city_name)
#first the program starts sfrom here 
if __name__ == "__main__":
    main()
