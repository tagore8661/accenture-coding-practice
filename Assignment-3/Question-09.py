# Question 9: Reverse a Number
class ReverseNumber:
    def __init__(self, number):
        self.number = number

    def reverse(self):
        return int(str(self.number)[::-1])

# Example: Reverse a Number
rn = ReverseNumber(987654)
print("Reversed Number:", rn.reverse())  # Output: 456789