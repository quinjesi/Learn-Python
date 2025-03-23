temp = int(input('Input temperature value e.g 39 (Celsius): '))

if temp >= 30:
	print('It is a hot day')
else:
	print('It is not a hot day')



name = input('Enter name: ')

if len(name) < 3:
	print('Name must be at least 3 characters')
elif len(name) > 20:
	print('Name must not exceed 20 characters')
else:
	print('Name is accepted!') 

