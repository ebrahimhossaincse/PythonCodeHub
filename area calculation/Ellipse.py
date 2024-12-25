import math

def area_ellipse(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

# Example
major_axis = 7
minor_axis = 5
print(f"Area of ellipse: {area_ellipse(major_axis, minor_axis):.2f}")
