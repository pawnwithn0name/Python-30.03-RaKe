num = int(input("Enter an integer: "))
# var = int(input("Enter an integer: "))



if num > 100:
	print("num is greater than 100.")
	if num > 200:
		print("num is greater than 200.")
	else:
		print("num is not greater than 200.")
else:
	print("num is not greater than 100.")
	if num > 50:
		print("num is greater than 50.")
	else:
		print("num is not greater than 50.")