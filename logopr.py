# AND OPERATOR
# Two Conditions
# E.g if applicant has high income and good credit, Eligible for loan
'''

# First method
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
	print("Eligible for loan")

# Second Method
high_income = input('Does applicant have high income(Yes or No): ').strip().lower()
good_credit = input('Does applicant have good credit(Yes or No): ').strip().lower()

if high_income == 'yes' and good_credit == 'yes':
	print('Eligible for loan')
elif high_income == 'no' and good_credit == 'no':
	print('Not eligible for loan')
else:
	print('Incorrect Option, try again')

'''


# OR OPERATOR

# First method
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
        print("Eligible for loan")

# Second Method
def con():
	while True:
		high_income = input('Does applicant have high income(Yes or No): ').strip().lower()
		good_credit = input('Does applicant have good credit(Yes or No): ').strip().lower()

		if high_income not in ('yes', 'no') or good_credit not in ('yes', 'no'):
			print('Incorrect Option. Please enter Yes or No')
			continue

		if high_income == 'yes' or good_credit == 'yes':
			print('Eligible for loan')
		else:
			print('Not Eligible for loan')

		another = input('Check another applicant? (Yes or No): ').strip().lower()
		if another != 'yes':
			print('Exiting...')
			break
con()



