def main():
	print("Enter two integers: ")
	var1 = int(input())
	var2 = int(input())
	opt = int(input("Select a math operation:\n1. \
Addition\n2. Subtraction\n"))
	if opt == 1:
		addn(var1, var2)
	elif opt == 2:
		subn(var1, var2)
	else:
		print("Enter a valid option")

def addn(one, two):
	sum = one + two
	print("sum of numbers {} & {} is {}".format(one, two, sum))
def subn(one, two):
	diff = one - two
	print("difference of numbers {} & {} is {}".format(one, two, diff))

if __name__ == "__main__": main()