# Question 12: Check for Prime Number
class PrimeChecker:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

# Example: Check for Prime Number
pc = PrimeChecker(29)
print("Is Prime:", pc.is_prime())  # Output: True