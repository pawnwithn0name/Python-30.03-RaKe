dict = {}
dict['one'] = "This is one"
dict[2]     = 2000

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales', 'address':'Thane', 'phone': '+982191212'}

#print(dict)

# Printing only Keys in dictionary
for k in tinydict.keys():
	print('Keys: ', k)


# Printing only Values in dictionary
for v in tinydict.values():
	print('Values: ', v)


# Printing Keys & Values both in dictionary
for k, v in tinydict.items():
	print('Keys: ', k, 'Values: ', v)

	
print(tinydict['phone'])
'''
print(tinydict.keys())
print(tinydict.values())

print(dict['one'])
'''
