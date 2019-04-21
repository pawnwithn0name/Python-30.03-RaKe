#list = ['physics', 'chemistry', 1997, 2000, 'biology', 'mathematics', 2020]

othr_list = [1,2,3,4,5,6,(55,66,77),7,8,9,0]

tup = (11,22,33,44,55)

#print ("Value available at index 2 : ", list[2])

#list[2] = 2001
#print ("New value available at index 2 : ", list[2])

#for i, elem in enumerate(list, start = 1):
#	print(i, ":",elem, end = ', ')
	
print(tup, type(tup))

some_list = list(tup)

print(some_list, type(some_list))

#print(list[::-1])

for itr in othr_list:
	if isinstance(itr, tuple):
		pass
	else: print(itr, end = ' ')

print()

for i in some_list:
	print(some_list.index(i), ': ', i)