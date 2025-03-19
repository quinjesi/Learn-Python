#If-else Conditions

is_hot = True
is_cold = True

if is_hot:
	print("It's a hot day!")
	print("Wear light clothes")
elif is_cold:
	print("It's a cold day!")
	print("Wear warm clothes")
else:
	print("It's a lovely day")
print("Enjoy your day")

#Exercise
price = 10 ** 6
print(f'Price of the house is {price} naira')

def credit():
	good_credit = input('Does the buyer have good credit?(Yes or No): ')

	if good_credit == "Yes":
		down_good = 0.10 * price
		print(f'The down payment is {down_good} naira')
	elif good_credit == "No":
		down_bad = 0.20 * price
		print(f'The down payment is {down_bad} naira')
	else:
		print('Incorrect Option!; Input Yes or No')
		credit()
credit()


