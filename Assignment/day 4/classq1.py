# Class Question 1
def kilometers_to_meter(km):
    return km * 1000    

def meter_to_centimeter(meter):
    return meter * 100

def centimeter_to_millimeter(cm):
    return cm * 10  

def fee_to_inches(feet):
    return feet * 12

def inches_to_centimeters(inches):
    return inches * 2.54

def distance_conversion(km, feet):
    meters = kilometers_to_meter(km)
    centimeters = meter_to_centimeter(meters)
    millimeters = centimeter_to_millimeter(centimeters)
    
    inches = fee_to_inches(feet)
    centimeters_from_inches = inches_to_centimeters(inches)
    
    return {
        "meters": meters,
        "centimeters": centimeters,
        "millimeters": millimeters,
        "inches": inches,
        "centimeters_from_inches": centimeters_from_inches
    }


# Example usage:
if __name__ == "__main__":
    km = 5
    feet = 10
    conversions = distance_conversion(km, feet)
    print(f"Conversions for {km} km and {feet} feet:")
    print(conversions)

