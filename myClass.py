# import requests
# import json
#
# city = input("Input city for Temperature: ")
# url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}"
#        "&appid=3bf43bfc7f398795202454021da742f5")
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# y = json.loads(response.text)
#
#
# def kelvin_to_f(y):
#     x = int(y["main"]["temp"])
#     results = (x - 273.15) * 9 / 5 + 32
#     return round(results)
#
#
# print(kelvin_to_f(y))
