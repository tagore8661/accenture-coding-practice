"""print(dir)
print(dir(__annotations__)) """

#Swapping Char

def Swap(string,chr1,chr2):
    result =""
    if string != None:
        result = string.replace(chr1,'*').replace(chr2,chr1).replace('*',chr2)
        return result
    else:
        return 'Null'

string = input()

chr1,chr2 = map(str,input().split())

print(Swap(string , chr1,chr2))