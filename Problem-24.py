# Find Dividend in given array

def find_index_dividend(arr,divisor,remainder,quotient):
    for index,dividend in enumerate(arr):
        if dividend // divisor == quotient and dividend % divisor == remainder:
            return index
    return -1
    
arr = [12,24,2,21]
divisor =8
remainder = 0
quotient = 3
index = find_index_dividend(arr,divisor,remainder,quotient)

print(index)