"""
1. Rectangle -

○ Write a program to take the length l and width w of a rectangle as input and calculate its area.
○ Expression: area = l * w

2. Triangle -

○ Write a program to take the base b and height h of a triangle as input and calculate its area.
○ Expression: area = 0.5 * b * h

3. Circle -

○ Write a program to take the radius r of a circle as input and calculate its area.
○ Expression: area = 3.14 * r * r (use π ≈ 3.14)

4. Trapezoid -

○ Write a program to take the lengths of the two bases a and b, and height h of a trapezoid as input and calculate its area.
○ Expression: area = 0.5 * (a + b) * h

5. Parallelogram -

○ Write a program to take the base b and height h of a parallelogram as input and calculate its area.
○ Expression: area = b * h
"""

#Area of a Rectangle
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
area_rectangle = l * w
print("Area of the rectangle:", area_rectangle)

#Area of a Triangle
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * b * h
print("Area of the triangle:", area_triangle)

#Area of a Circle
r = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * r * r
print("Area of the circle:", area_circle)

#Area of a Trapezoid
a = float(input("Enter the first base of the trapezoid: "))
b = float(input("Enter the second base of the trapezoid: "))
h = float(input("Enter the height of the trapezoid: "))
area_trapezoid = 0.5 * (a + b) * h
print("Area of the trapezoid:", area_trapezoid)

#Area of a Parallelogram
b = float(input("Enter the base of the parallelogram: "))
h = float(input("Enter the height of the parallelogram: "))
area_parallelogram = b * h
print("Area of the parallelogram:", area_parallelogram)

