num = float(input("Enter a floating-point: "))
var = int(input("Enter an integer: "))



if num > 100:
	print("Numbers entered: {}, {} is greater than 100.".format(num, var))
	print("Numbers entered: {1}, {0} is greater than 100.".format(num, var))
	print(f"Numbers entered: {num}, {var} is greater than 100.")
	print("Numbers entered: %d, %f is greater than 100." %(num, var))