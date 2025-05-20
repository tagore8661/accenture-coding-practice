# Question 7: Largest Subarray with Equal 0s and 1s
class LargestEqualSubarray:
    def __init__(self, array):
        self.array = array

    def largest_subarray(self):
        map_ = {0: -1}
        max_len = 0
        sum_ = 0
        for i in range(len(self.array)):
            sum_ += 1 if self.array[i] == 1 else -1
            if sum_ in map_:
                max_len = max(max_len, i - map_[sum_])
            else:
                map_[sum_] = i
        return max_len
    
# Example: Largest Subarray with Equal 0s and 1s
les = LargestEqualSubarray([1, 0, 1, 1, 1, 0, 0])
print("Largest Subarray Length:", les.largest_subarray())  # Output: 6