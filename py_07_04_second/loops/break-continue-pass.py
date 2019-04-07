'''
for letter in 'Python':
	if letter == 'h':
		break
	print ('Current Letter :', letter)

for i in range(1,11):
	if i == 8:
		print("break statement encountered!")
		break
	print(i)

i = 10
while i > 0:
	i = i - 1
	if i == 4:
		print("continue statement encountered!")
		continue
	print(i)
	
for letter in 'Python':
	if letter == 'h':
		print("continue statement encountered!")
		continue
	print ('Current Letter :', letter)
'''
def func_2():
	pass
	
def func_1():
	for letter in 'Python':
		if letter == 'h':
			print("pass statement encountered!")
			pass
		print ('Current Letter :', letter)
	func_2()
	
func_1()


'''
	
'''
	