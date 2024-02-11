x = input("Enter number 1: ")
y = input("Enter number 2: ")

try:
     z = int(x) / int(y)
     a = 'baby yoda' + 56 

except ZeroDivisionError as e:
     print("Exception occured", e)
     z = 0

except TypeError as te:
     print("Exception occured: ", te)

except Exception as e: 
     print("Generic exception handling")



print("division is: ", z)
