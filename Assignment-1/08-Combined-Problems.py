"""
1. Surface Area and Volume of a Cylinder -

○ Write a program to take the radius r and height h of a cylinder as input and calculate both its surface area and volume.
○ Expressions:
  ▪ surface_area = 2 * 3.14 * r * (r + h) (use π ≈ 3.14)
  ▪ volume = 3.14 * r * r * h

2. Surface Area and Volume of a Sphere -

○ Write a program to take the radius r of a sphere as input and calculate both its surface area and volume.
○ Expressions:
  ▪ surface_area = 4 * 3.14 * r * r (use π ≈ 3.14)
  ▪ volume = (4.0 / 3.0) * 3.14 * r * r * r
"""

#1. Surface Area and Volume of a Cylinder
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
surface_area_cylinder = 2 * 3.14 * r * (r + h)
volume_cylinder = 3.14 * r * r * h
print("Surface area of the cylinder:", surface_area_cylinder)
print("Volume of the cylinder:", volume_cylinder)


#2. Surface Area and Volume of a Sphere
r = float(input("Enter the radius of the sphere: "))
surface_area_sphere = 4 * 3.14 * r * r
volume_sphere = (4.0 / 3.0) * 3.14 * r * r * r
print("Surface area of the sphere:", surface_area_sphere)
print("Volume of the sphere:", volume_sphere)