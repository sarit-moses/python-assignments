import math
import argparse

### values:
parser = argparse.ArgumentParser()
parser.add_argument('radius', type=int)
args = parser.parse_args()
radius = args.radius
#radius = float(input("What is the radius of the circle?"))
pi_val = math.pi

# print area:
print("circle area:", pi_val*(radius**2))
# print circumference:
print("circle circumference:", 2*pi_val*radius)
