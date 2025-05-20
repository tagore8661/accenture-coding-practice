# Question 3: Maximum Sum of Contiguous Subarray
class MaximumSubarraySum:
    def __init__(self, array):
        self.array = array

    def max_sum(self):
        max_current = max_global = self.array[0]
        for i in range(1, len(self.array)):
            max_current = max(self.array[i], max_current + self.array[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

# Example: Maximum Sum of Contiguous Subarray
mss = MaximumSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Maximum Subarray Sum:", mss.max_sum())  # Output: 6