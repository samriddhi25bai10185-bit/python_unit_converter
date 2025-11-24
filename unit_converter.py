def length_converter():
    print("\nLength Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} m = {value/1000} km")
    elif choice == "2":
        print(f"{value} km = {value*1000} m")
    elif choice == "3":
        print(f"{value} cm = {value/100} m")
    elif choice == "4":
        print(f"{value} m = {value*100} cm")
    else:
        print("Invalid option!")


def weight_converter():
    print("\nWeight Converter")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")
    print("3. Pound to Kilogram")
    print("4. Kilogram to Pound")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} g = {value/1000} kg")
    elif choice == "2":
        print(f"{value} kg = {value*1000} g")
    elif choice == "3":
        print(f"{value} lb = {value*0.453592} kg")
    elif choice == "4":
        print(f"{value} kg = {value/0.453592} lb")
    else:
        print("Invalid option!")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == "2":
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == "3":
        print(f"{value}°C = {value + 273.15} K")
    elif choice == "4":
        print(f"{value} K = {value - 273.15}°C")
    else:
        print("Invalid option!")

def time_converter():
    print("\n--- Time Converter ---")
    print("1. Seconds → Minutes")
    print("2. Minutes → Seconds")
    print("3. Hours → Minutes")
    print("4. Minutes → Hours")

    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"{value} s = {value/60} min")
    elif choice == "2":
        print(f"{value} min = {value*60} s")
    elif choice == "3":
        print(f"{value} hr = {value*60} min")
    elif choice == "4":
        print(f"{value} min = {value/60} hr")
    else:
        print("Invalid option!")


def main():
    while True:
        print("\nUNIT CONVERTER")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Time")
        print("5. Exit")

        choice = input("Choose category: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            time_converter()
        elif choice == "5":
            print("Thankyou!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
