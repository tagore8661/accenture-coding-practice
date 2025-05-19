"""
bouncing ball,
return no.of distance the ball travels

formula: h*pow(en, 2)

en=velocity/no.of bounce

i/p: height:10,
     velocity:20,
     bounce:5

O/p: 160
"""

def calculate_distance(height, velocity, bounce):
    en = velocity / bounce
    distance = height * pow(en, 2)
    #distance = height * (en**2)
    return distance

# Example usage:
height = 10
velocity = 20
bounce = 5
result =int(calculate_distance(height, velocity, bounce))
print(result)  # Output will be 160