# Class Question 2
#conversion km to m, m to cm, cm to mm, feet to inches, inches to cm
# using lambla functions

kilometers_to_meter = lambda km: km * 1000
meter_to_centemeter = lambda meter: meter * 100
centimeter_to_milimeter = lambda cm: cm * 10
feet_to_inches = lambda feet: feet * 12
inches_to_centemeter = lambda inches: inches * 2.54


print(f"Meters: {kilometers_to_meter(3)}")
#
print(f"Centimeters: {meter_to_centemeter(kilometers_to_meter(3))}")

print(f"Millimeters: {centimeter_to_milimeter(meter_to_centemeter(kilometers_to_meter(3)))}")

print(f"inches: {feet_to_inches(5)}")

print(f"Centimeters from inches: {inches_to_centemeter(feet_to_inches(5))}")
 
