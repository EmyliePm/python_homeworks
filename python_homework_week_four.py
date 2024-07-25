# Exercise 1
weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.

city = weather["city"]
country = weather["country"]
temperature_celsius = weather["temperature"]
temperature_fahrenheit = temperature_celsius * 9/5 + 32
humidity = weather["humidity"]

print(f"It is {temperature_celsius:.0f}ºC ({temperature_fahrenheit:.0f}ºF) in {city}, {country}, and the humidity level is {humidity}%.")

# Exercise 2
forecast = {
  "city":"Lisbon",
  "country":"Portugal",
  "daily":
    [
      17.76,
      13.08,
      12.14,
      11.25,
      14.29
    ]
}

# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC

print(f"The forecast for {forecast['city']}, {forecast['country']} for the next 5 days is:")

day = 1

for temperature in forecast['daily']:
    print(f"Day {day}: {temperature:.0f}ºC")
    day += 1