list = ['abcd', 786, 2.23, 'john', 70.2]

tinylist = [123, 'john']

#for(int i = 0; i < list.len; i ++)
for i in reversed(list):
	print (i, end = ' ')

print()
list[0] = 'wxyz'

for i in reversed(list):
	print (i, end = ' ')

'''
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
'''