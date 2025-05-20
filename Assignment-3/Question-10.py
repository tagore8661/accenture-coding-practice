# Question 10: Largest Number in an Array
class LargestNumber:
    def __init__(self, array):
        self.array = array

    def find_largest(self):
        return max(self.array)

# Example: Largest Number in an Array
ln = LargestNumber([1, 4, 6, 7, 8, 9])
print("Largest Number:", ln.find_largest())  # Output: 9