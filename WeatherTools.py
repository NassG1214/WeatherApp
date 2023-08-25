
# def kelvin_to_f(key: str):
#     f_temp = int(api_searcher["main"][key])
#     results = (f_temp - 273.15) * 9 / 5 + 32
#     return f'{round(results)} °F'
#
#
# def kelvin_to_c(key: str):
#     c_temp = int(api_searcher["main"][key])
#     results = c_temp - 273.15
#     return f'{round(results)} °C'
#
#
# def kelvin_to_f_c(key: str):
#     return kelvin_to_f(key) + kelvin_to_c(key)
#
#
# def temperature():
#     value = input("Enter one of the following to see the temperature: "
#                   "temp, feels_like, min temp, max temp, pressure, and humidity"
#                   "for all type all.")
#     if (value == "all"):
#         kelvin_to_f_c("temp")
#         kelvin_to_f_c("feels_like")
#         kelvin_to_f_c("min temp")
#         kelvin_to_f_c("max temp")
#         kelvin_to_f_c("pressure")
#         kelvin_to_f_c("humidity")
#     else:
#         kelvin_to_f_c(value)
