import requests

def get_weather(city_name):
    """
    Fetches weather information for a given city using WeatherAPI.com.

    Args:
        city_name (str): The name of the city to get weather for.

    Returns:
        dict or None: A dictionary containing weather information if successful,
                      otherwise None.
    """
    # IMPORTANT: Replace 'YOUR_API_KEY' with your actual API key from WeatherAPI.com
    # You can get one for free at https://www.weatherapi.com/
    api_key = '9e8f8e16026d4ac252c78dd5fd0cdfdf'
    base_url = "http://api.weatherapi.com/v1/current.json"

    # Construct the parameters for the API request
    params = {
        'key': api_key,
        'q': city_name
    }

    try:
        # Make the GET request to the weather API
        response = requests.get(base_url, params=params)

        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        location = weather_data['location']['name']
        country = weather_data['location']['country']
        temp_c = weather_data['current']['temp_c']
        temp_f = weather_data['current']['temp_f']
        condition = weather_data['current']['condition']['text']
        feels_like_c = weather_data['current']['feelslike_c']
        feels_like_f = weather_data['current']['feelslike_f']
        humidity = weather_data['current']['humidity']
        wind_kph = weather_data['current']['wind_kph']
        wind_mph = weather_data['current']['wind_mph']
        wind_dir = weather_data['current']['wind_dir']

        # Return a structured dictionary of the weather info
        return {
            'location': f"{location}, {country}",
            'temperature_celsius': temp_c,
            'temperature_fahrenheit': temp_f,
            'condition': condition,
            'feels_like_celsius': feels_like_c,
            'feels_like_fahrenheit': feels_like_f,
            'humidity': humidity,
            'wind_kph': wind_kph,
            'wind_mph': wind_mph,
            'wind_direction': wind_dir
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Could not parse weather data. Missing key: {key_err}")
        print(f"Full API response: {weather_data}")
    return None

if __name__ == "__main__":
    # Example usage:
    city = input("Enter city name: ")
    weather_info = get_weather(city)

    if weather_info:
        print("\n--- Current Weather Information ---")
        print(f"Location: {weather_info['location']}")
        print(f"Condition: {weather_info['condition']}")
        print(f"Temperature: {weather_info['temperature_celsius']}°C ({weather_info['temperature_fahrenheit']}°F)")
        print(f"Feels like: {weather_info['feels_like_celsius']}°C ({weather_info['feels_like_fahrenheit']}°F)")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind: {weather_info['wind_kph']} kph ({weather_info['wind_mph']} mph) from {weather_info['wind_direction']}")
    else:
        print("Failed to retrieve weather information.")
