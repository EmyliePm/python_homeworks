city = input("Enter a city name: ")


if city == "":
    print("Please enter a city and try again")
else:
    temp_input = input("Enter the temperature: ")


    if temp_input == "":
        print("Please enter the temperature and try again")
    else:
        try:
            temperature = int(temp_input)
            if temperature >= 20:
                print(f"It is currently warm in {city} with a temperature of {temperature} ºC")
            elif temperature > 10:
                print(f"It is currently chilly in {city} with a temperature of {temperature} ºC")
            elif temperature < 10:
                print(f"It is currently cold in {city} with a temperature of {temperature} ºC")
        except ValueError:
            print("Please enter a valid number for the temperature and try again")