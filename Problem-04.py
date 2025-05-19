"""You are required to implement the following function:

int CountSpecificNumbers(int m, int n);

The function accepts two arguments m and n which are integers. You are required to calculate 
the count of numbers having only 1, 4 and 9 as their digits between the numbers lying in the 
range m and n both inclusive, and return the same. Return -1 if m>n."""


def countSpecificNumbers(m,n):

    if m>n:

        return -1

    count = 0

    for i in range(m,n+1):

        num = i

        flag = True

        while num>0:

            digit = num%10   #digit seperation logic

            num //= 10

            if digit==1 or digit==4 or digit==9:

                continue

            else:

                flag = False

                break

        if flag:

            count += 1

    return count

m = int(input())

n = int(input())

print(countSpecificNumbers(m,n))


#another way

def CountSpecificNumbers(m, n):
    # Return -1 if m is greater than n
    if m > n:
        return -1
    
    # Initialize count to 0
    count = 0
    
    # Loop through each number in the range [m, n]
    for number in range(m, n + 1):
        # Convert the number to a string to check each digit
        num_str = str(number)
        
        # Check if all digits in the number are either '1', '4', or '9'
        if all(digit in '149' for digit in num_str):
            # If true, increment the count
            count += 1
    
    # Return the final count
    return count

result = CountSpecificNumbers(100, 200)
print(result)  # Output should be the count of numbers with only digits 1, 4, and 9