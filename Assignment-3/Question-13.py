# Question 13: Find Target Element in an Array
class FindTarget:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def find(self):
        for i, value in enumerate(self.array):
            if value == self.target:
                return i
        return -1

# Example: Find Target Element in an Array
ft = FindTarget([2, 3, 4, 10, 40], 10)
print("Target Index:", ft.find())  # Output: 3