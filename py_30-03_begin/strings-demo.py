str		=	input('Enter 1st String: ')
str1	=	input('Enter 2nd String: ')
print ('First STRING Entered: ',str )
print('Second STRING Entered: ', str1)
print('Reverse String = ', '\n',(str[::-1]), '\n', str1[::-1])
print("Before Swap: ",str,str1)
str, str1 = str1, str
print("After First Swap: ",str,str1)

temp = str
str = str1
str1 = temp

print("After Second Swap: ",str,str1)