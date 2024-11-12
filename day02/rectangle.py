def rec_area(width: float, length: float) -> float:
    """ this function receives the width and the length of a rectangle, 
    and returns its area"""
    return width*length

def rec_circumference(width: float, length: float) -> float:
    """ this function reveives the width and the length of a rectangle, 
    and returns its circumference"""
    return 2*(width+length)

def print_rec_areas(width: float, length: float):
    """ this function prints the area and circumference of a giver rectangle """
    print("rectangle area:", rec_area(width, length))
    print("rectangle circumference:", rec_circumference(width, length))


print_rec_areas(3, 4)