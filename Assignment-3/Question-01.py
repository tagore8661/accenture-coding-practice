# Question 1: Next Greater Element
class NextGreaterElement:
    def __init__(self, array):
        self.array = array

    def find_next_greater(self):
        result = [-1] * len(self.array)
        stack = []
        for i in range(len(self.array)):
            while stack and self.array[stack[-1]] < self.array[i]:
                index = stack.pop()
                result[index] = self.array[i]
            stack.append(i)
            
        return result

# Example: Next Greater Element
nge = NextGreaterElement([4, 5, 2, 25])
print("Next Greater Element:", nge.find_next_greater())  # Output: [5, 25, 25, -1]