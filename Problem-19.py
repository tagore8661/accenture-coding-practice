"""You are required to input the size of the matrix then the elements of matrix, 
then you have to divide the main matrix in two sub matrices (even and odd) 
in such a way that element at 0 index will be considered as even and element at 1st index will be considered as odd and so on.
then you have sort the even and odd matrices in ascending order then print the sum of second largest number from both the matrices"""

def Matrix(n):
    array = []
    even_arr =[]
    odd_arr =[]
    for i in range(n):
        print(f"enter element at {i} index :")
        value = int(input())
        array.append(value)
        if i % 2 == 0 :
            even_arr.append(value)
        else:
            odd_arr.append(value)
    even_sort = sorted(even_arr)
    odd_sort= sorted(odd_arr)
    print("ARRAY=",array)
    print("EVEN ARRAY=",even_sort)
    print("ODD ARRAY=",odd_sort)
    sum= even_sort[len(even_arr)-2] + odd_sort[len(odd_arr)-2]
    print("sum of second largest number from both the matrices",sum)

n=int(input("enter the size of array : "))
print(Matrix(n))