def can_place_flowers(flowerbed):
    count = 0
    n = len(flowerbed)
    
    for i in range(n):
        if flowerbed[i] == 0:
            # Check if the previous and next positions are also empty or out of bounds
            if (i == 0 or flowerbed[i - 1] == 0) and (i == n - 1 or flowerbed[i + 1] == 0):
                # Plant a flower here
                flowerbed[i] = 1
                count += 1
    
    return count

# Example usage
flowerbed = [1, 0, 0, 0, 1]
print(f"Number of additional flowers that can be planted: {can_place_flowers(flowerbed)}")
