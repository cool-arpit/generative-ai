# Create a program to convert temperature from celcius to fahrenheit and vice versa.
def Temp_change(temp_value, unit):
    if unit == "C" or unit == "c":
        temperature = round(temp_value*9/5 +32)
        print(f"The temperature for {temp_value} deg celcius in fahrenheit is:" , str(temperature) + "F")
    elif unit == "F" or unit =="f":
        temperature = round((temp_value-32)*5/9)
        print(f"The temperature for {temp_value} deg fahrenheit in celcius is:" , str(temperature) + "C")
    else:
        print("Invalid input")

temp_value = float(input("ENTER TEMPERATURE :"))
unit = input("ENTER UNIT (C/F)")
Temp_change(temp_value , unit)