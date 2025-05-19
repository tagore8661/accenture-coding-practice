"""Your friend has made entry of a name in the form first name F and 
last name L in your contact list. But some letters are in uppercase 
while others are in lowercase. Your task is to find and return a streng 
representing the names such that the first name of your contacts is 
in lowercase, and the last name of your contact is in uppercase """

f = input("Enter First Name:")
l = input("Enter Last Name:")

print(f.lower()+" "+l.upper())