user_name = input("What is your name? ")
user_city = input("What city are you in? ")
user_temperature = input("What is the current temperature in celcius? ")
temp_farenheight = (float(user_temperature) * 9 / 5) + 32
night_temp_celcius = float(user_temperature) - 10
night_temp_farenheight = (float(night_temp_celcius) * 9 / 5) + 32

print(
    f"Hi {user_name}, you are in {user_city}, and it is currently {user_temperature} ºC, or {temp_farenheight} ºF."
)
print(
    f"I predict the temperature will reach {night_temp_celcius:.2f} ºC at night, or {night_temp_farenheight:.2f} ºF "
)
print("Have a good day!")
#Display this sentence:
#Hi Matt, you are in Lisbon, and it is currently 12ºC or 30ºF).
#Then display
#I predict that tonight, the temperature will reach 2ºC or 12ºF).
#Finally, display
#Have a good day!
