#floyds triangle

def print_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()

n = int(input())
print_pattern(n)