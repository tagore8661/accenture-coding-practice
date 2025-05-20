# Question 4: Nearest Integer Divisible by m
class NearestInteger:
    def __init__(self, num, m):
        self.num = num
        self.m = m

    def nearest_divisible(self):
        lower = (self.num // self.m) * self.m
        higher = lower + self.m
        return lower if abs(self.num - lower) <= abs(self.num - higher) else higher

# Example: Nearest Integer Divisible by m
ni = NearestInteger(67, 8)
print("Nearest Divisible Integer:", ni.nearest_divisible())  # Output: 64