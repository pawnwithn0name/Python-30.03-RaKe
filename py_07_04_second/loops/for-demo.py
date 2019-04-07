n_list = [1,2,3,4,5,6,7,8,9,10]
r1 = range(1500, 3001)


result_list = []

print(r1)

for i in r1:
	if i % 7 == 0 and i % 5 == 0:
		result_list.append(i)

print(result_list)

'''
for i in r1:
	print('Range Element: ', i)
'''

'''
1500 to 3000
print the integers that are divisible by 7 and multiples of 5.
'''

