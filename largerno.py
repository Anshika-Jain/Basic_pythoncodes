print("Enter first number:")
a = float(input())
print("Enter second number:")
b = float(input())
print("Enter third number:")
c = float(input())
 
if (a > b) and (a > c):
   largest = a
elif (b > a)and (b > c):
   largest = b
else:
   largest = c
 
print("The largest number is",largest)
