#absolute difference of less than or equal to ‘diff’ with ‘num’.

def findCount( arr,n, num, diff):
    count=0
    for i in range(n):
        if(abs(arr[i]-num)<=diff):
            count+=1
    
    return count
arr=list(map(int,input().split()))
n=len(arr)
num=int(input())
diff=int(input())
print(findCount(arr,n, num, diff))