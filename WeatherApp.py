import requests
import json


def greetings():
    while True:
        key = input("For the keys, choose from these options: \n"
                    "coord, weather, main (temperature), visibility, wind, clouds, sys(info of city)\n"
                    "If finished please hit the enter key or type \"stop\" \n\n")
        if key == "" or key == "stop":
            break
        greeting_key_options(key)


def data_searcher(key: str, value: str):
    data = api_searcher[key][value]
    return f"{value}:\t {data}"


def greeting_key_options(key: str):
    while True:
        if key == "coord":
            value = input("Choose from the following: lon (longitude), lat (Latitude)"
                          "\t\n If finished please hit the enter key or type \"stop\"   \n")
            if value == "" or value == "stop":
                break
            else:
                print(data_searcher(key, value))
        if key == "weather":
            value = input("Choose from the following: id, main (general description), description"
                          "\t\n If finished please hit the enter key or type \"stop\"   \n")
            if value == "" or value == "stop":
                break
            else:
                print(api_searcher["weather"][0][value])
        if key == "main":
            temperature()
        if key == "visibility":
            print(api_searcher["visibility"])
            break

        if key == "wind":
            value = input("Choose from the following: speed, deg"
                          "\t\n If finished please hit the enter key or type \"stop\"   \n")
            if value == "" or value == "stop":
                break
            else:
                print(data_searcher(key, value))
        if key == "clouds":
            data_searcher(key, "all")
            break
        if key == "sys":
            value = input("Choose from the following: type, id, country, sunrise, sunset"
                          "\t\n If finished please hit the enter key or type \"stop\"   \n")
            if value == "" or value == "stop":
                break
            else:
                print(data_searcher(key, value))


def kelvin_to_f(key: str):
    f_temp = int(api_searcher["main"][key])
    results = (f_temp - 273.15) * 9 / 5 + 32
    return f'{round(results)} °F'


def kelvin_to_c(key: str):
    c_temp = int(api_searcher["main"][key])
    results = c_temp - 273.15
    return f'{round(results)} °C'


def kelvin_to_f_c(key: str):
    return f"{key}:\t {kelvin_to_f(key)} \t {kelvin_to_c(key)}"


def temperature():
    value = input("Enter one of the following to see the temperature: \n"
                  "temp, feels_like, min temp, max temp, pressure, and humidity"
                  " for all type all.\n")
    if value == "all":
        print(kelvin_to_f_c("temp"))
        print(kelvin_to_f_c("feels_like"))
        print(kelvin_to_f_c("temp_min"))
        print(kelvin_to_f_c("temp_max"))
        print(data_searcher("main", "pressure"))
        print(data_searcher("main", "humidity"))
    elif value == "pressure" or value == "humidity":
        data_searcher("main", value)
    else:
        print(kelvin_to_f_c(value))


city = input("Input city\n")
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}"
       "&appid=3bf43bfc7f398795202454021da742f5")

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Loads the information based on inputs such as city
api_searcher = json.loads(response.text)

greetings()
