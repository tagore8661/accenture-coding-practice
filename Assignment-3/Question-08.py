# Question 8: Count Magical Numbers
class MagicalNumbers:
    def __init__(self, n):
        self.n = n

    def count_magical(self):
        count = 0
        for i in range(1, self.n + 1):
            binary = bin(i)[2:]
            modified = binary.replace('1', '2').replace('0', '1')
            digit_sum = sum(int(ch) for ch in modified)
            if digit_sum % 2 == 1:
                count += 1
        return count
    
# Example: Count Magical Numbers
mn = MagicalNumbers(5)
print("Count of Magical Numbers:", mn.count_magical())  # Output: 2