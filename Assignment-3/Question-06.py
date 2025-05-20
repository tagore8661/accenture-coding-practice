# Question 6: Minimum Steps to Climb Stairs
class MinimumSteps:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def min_steps(self):
        return self.n // self.m + (self.n % self.m != 0)

# Example: Minimum Steps to Climb Stairs
ms = MinimumSteps(5, 2)
print("Minimum Steps:", ms.min_steps())  # Output: 3

#Anather Way
def Mini(n,m):
    steps = n // m
    if n % m != 0:
        steps += (n % m)
    return steps

print(Mini(5,2))