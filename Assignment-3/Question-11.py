# Question 11: Subarray with Largest Sum
class LargestSumSubarray:
    def __init__(self, array):
        self.array = array

    def max_sum(self):
        max_current = max_global = self.array[0]
        for i in range(1, len(self.array)):
            max_current = max(self.array[i], max_current + self.array[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
    
# Example: Subarray with Largest Sum
lss = LargestSumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Largest Subarray Sum:", lss.max_sum())  # Output: 6