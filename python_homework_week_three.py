def calculate_fahrenheit_temperature(temp_input):
  """Calculates the farenheit value from celsius value."""
  farenheit_temperature = (float(temp_input) * 9 /5) + 32

  return farenheit_temperature


def message(city_input, temp_input,):
  """Shows message"""
  fahrenheit_temperature = calculate_fahrenheit_temperature(temp_input)   
  print(f"It is currently {temp_input}ºC ({round(fahrenheit_temperature)}ºF) in {city_input}")

city_input = input("Enter the name of the city: ")
temp_input = input(f"Enter the temperature in {city_input.capitalize()}: ")
if city_input and temp_input:
  message(city_input, temp_input)
else:
  print("You did not enter a city and/or temperature")

