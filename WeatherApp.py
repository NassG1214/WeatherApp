import requests


def get_location_from_user():
    while True:  # Loop until valid input is received
        try:
            prompt = input("Input city with state, e.g., 'Miami, Florida, US'; 'London, England, GB':\n").strip()
            if not prompt:
                print("Input cannot be blank. Please enter the city, state, and country code.")
                continue
            parts = [part.strip() for part in prompt.split(",")]
            if len(parts) < 3:
                print("Incomplete information. Please make sure to input city, state, and country code.")
                continue
            return {"city": parts[0], "state_code": parts[1], "country_code": parts[2]}
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def fetch_geolocation(city, state_code, country_code):
    geo_url = (f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&appid"
               f"=3bf43bfc7f398795202454021da742f5")
    response = requests.get(geo_url).json()
    if not response:
        print("Could not find the location. Please check the inputs and try again.")
        return None, None
    return response[0]['lat'], response[0]['lon']


def fetch_weather_data(lat, lon):
    if lat is None or lon is None:  # Skip request if geolocation failed
        return None
    weather_url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid"
                   f"=3bf43bfc7f398795202454021da742f5")
    response = requests.get(weather_url).json()
    if response.get('cod') != 200:
        print("Failed to fetch weather data. Please try again later.")
        return None
    return response


def kelvin_to_fahrenheit(kelvin):
    return f"{(kelvin - 273.15) * 9 / 5 + 32:.2f}"


def kelvin_to_celsius(kelvin):
    return f"{kelvin - 273.15:.2f}"


def print_weather_data(data):
    if not data:
        return  # Skip if no data
    key_mapping = {
        "coord": ["lon", "lat"],
        "weather": ["id", "main", "description"],
        "main": ["temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity"],
        "visibility": [],
        "wind": ["speed", "deg"],
        "clouds": ["all"],
        "sys": ["type", "id", "country", "sunrise", "sunset"],
    }

    key = input(
        "Choose from the following keys: coord, weather, main (temperature), visibility, wind, clouds, sys (info of "
        "city). Type 'stop' to finish:\n").lower()
    while key != "stop":
        if key in key_mapping:
            process_weather_data_choice(data, key, key_mapping)
        else:
            print("Invalid key, please try again.")
        key = input("Choose another key or type 'stop' to finish:\n").lower()


def process_weather_data_choice(data, key, key_mapping):
    if key == "main":
        for sub_key in key_mapping[key]:
            if sub_key in ["temp", "feels_like", "temp_min", "temp_max"]:
                print(
                    f"{sub_key}: {kelvin_to_fahrenheit(data[key][sub_key])}F / {kelvin_to_celsius(data[key][sub_key])}C")
            else:
                print(f"{sub_key}: {data[key][sub_key]}")
    elif key == "visibility":
        print(f"Visibility: {data[key]} meters")
    else:
        for sub_key in key_mapping[key]:
            print(f"{sub_key}: {data[key][sub_key] if key != 'weather' else data[key][0][sub_key]}")


def main():
    location = get_location_from_user()
    if not location:
        return  # End if the location input was invalid
    lat, lon = fetch_geolocation(**location)
    if lat is None or lon is None:
        return  # End if the geolocation lookup failed
    weather_data = fetch_weather_data(lat, lon)
    if not weather_data:
        return  # End if the weather data fetch failed
    print_weather_data(weather_data)


if __name__ == "__main__":
    main()
