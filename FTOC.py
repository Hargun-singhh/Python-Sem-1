temp = float(input("Enter the Temperature:"))
unit = str(input("Enter the Unit (C/F) :"))

if unit == "C":
    f = (temp - 32) * 5 / 9
    print("----------RESULT------------")
    print("Temperature in Fahrenheit:", f)
    print("----------------------------")

else:
    c = (temp * 9 / 5) + 32
    print("--------RESULT-----------")
    print("Temperature in Celsius:", c)
    print("-------------------------")
