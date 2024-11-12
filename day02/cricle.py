import math
pi_val = math.pi

def cir_area(radius: float) -> float:
    """ this function receives the width and the length of a circle, 
    and returns its area"""
    return pi_val*(radius**2)

def cir_circumference(radius: float) -> float:
    """ this function reveives the width and the length of a circle, 
    and returns its circumference"""
    return 2*pi_val*radius

def print_cir_areas(radius: float):
    """ this function prints the area and circumference of a giver circle """
    print("circle area:", cir_area(radius))
    print("circle circumference:", cir_circumference(radius))



print(cir_area(1))
print(cir_circumference(1))

print_cir_areas(1)


