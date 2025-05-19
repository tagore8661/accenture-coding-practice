"""
1. Cuboid -

○ Write a program to take the length l, width w, and height h of a cuboid as input and calculate its volume.
○ Expression: volume = l * w * h

2. Cube -

○ Write a program to take the side length a of a cube as input and calculate its volume.
○ Expression: volume = a * a * a

3. Cylinder -

○ Write a program to take the radius r and height h of a cylinder as input and calculate its volume.
○ Expression: volume = 3.14 * r * r * h (use π ≈ 3.14)

4. Sphere -

○ Write a program to take the radius r of a sphere as input and calculate its volume.
○ Expression: volume = (4.0 / 3.0) * 3.14 * r * r * r (use π ≈ 3.14)

5. Cone -

○ Write a program to take the radius r and height h of a cone as input and calculate its volume.
○ Expression: volume = (1.0 / 3.0) * 3.14 * r * r * h (use π ≈ 3.14)
"""

#Volume of a Cuboid
l = float(input("Enter the length of the cuboid: "))
w = float(input("Enter the width of the cuboid: "))
h = float(input("Enter the height of the cuboid: "))
volume_cuboid = l * w * h
print("Volume of the cuboid:", volume_cuboid)

#Volume of a Cube
a = float(input("Enter the side length of the cube: "))
volume_cube = a * a * a
print("Volume of the cube:", volume_cube)

#Volume of a Cylinder
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
volume_cylinder = 3.14 * r * r * h
print("Volume of the cylinder:", volume_cylinder)

#Volume of a Sphere
r = float(input("Enter the radius of the sphere: "))
volume_sphere = (4.0 / 3.0) * 3.14 * r * r * r
print("Volume of the sphere:", volume_sphere)

#Volume of a Cone
r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))
volume_cone = (1.0 / 3.0) * 3.14 * r * r * h
print("Volume of the cone:", volume_cone)
