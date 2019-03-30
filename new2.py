a = int (input("enter the first integer: "))
b = int (input("enter the second integer: "))
 
print("values before swapping : {} {} ".format(a, b))
 
a = a  + b
b = a - b
a = a - b 
 
print("values after swapping : {} {} ".format(a, b))

if a > b:
	print(" IF condition is true")
else  :
	print("ELSE condition is true")