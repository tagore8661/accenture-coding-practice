# Question 2: Push Zeros to the End
class PushZeros:
    def __init__(self, array):
        self.array = array

    def move_zeros(self):
        non_zero_index = 0
        for i in range(len(self.array)):
            if self.array[i] != 0:
                self.array[non_zero_index], self.array[i] = self.array[i], self.array[non_zero_index]
                non_zero_index += 1
        return self.array
    
# Example: Push Zeros to the End
pz = PushZeros([1, 2, 0, 4, 3, 0, 5, 0])
print("Array after pushing zeros:", pz.move_zeros())  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

#Another Way
def Push(arr):
    out = []
    for i in range(len(arr)):
        if arr[i] != 0:
            out.append(arr[i])
    while len(out) != len(arr):
        out.append(0)

    return out

print(Push([1,2,0,0,0,3,6]))